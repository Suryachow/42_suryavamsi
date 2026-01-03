from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from rag_service import RAGService
from billing_service import BillingService
from recharge_service import RechargeService
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# Global service instances
rag_service = None
billing_service = None
recharge_service = None

def get_rag_service():
    global rag_service
    if rag_service is None:
        rag_service = RAGService()
    return rag_service

def get_billing_service():
    global billing_service
    if billing_service is None:
        billing_service = BillingService()
    return billing_service

def get_recharge_service():
    global recharge_service
    if recharge_service is None:
        recharge_service = RechargeService()
    return recharge_service

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    query = data.get("message")
    api_key = data.get("apiKey")
    
    if not query:
        return jsonify({"error": "No message provided"}), 400

    rag = get_rag_service()
    billing = get_billing_service()
    recharge = get_recharge_service()
    
    # Check query type
    billing_keywords = ["bill", "payment", "due", "pay", "invoice", "amount", "balance", "pending"]
    recharge_keywords = ["recharge", "plan", "prepaid", "postpaid", "topup", "top up", "data", "validity"]
    
    is_billing_query = any(keyword in query.lower() for keyword in billing_keywords)
    is_recharge_query = any(keyword in query.lower() for keyword in recharge_keywords)
    
    if is_recharge_query:
        # Get recharge plans information
        recharge_context = recharge.search_plans(query)
        
        # Enhance RAG query with recharge context
        enhanced_query = f"AVAILABLE PLANS:\n{recharge_context}\n\nUSER QUERY: {query}"
        result = rag.answer_query(enhanced_query, api_key=api_key)
    
    elif is_billing_query:
        # Get billing information
        billing_context = billing.search_bills(query)
        
        # Enhance RAG query with billing context
        enhanced_query = f"USER BILLING DATA:\n{billing_context}\n\nUSER QUERY: {query}"
        result = rag.answer_query(enhanced_query, api_key=api_key)
    
    else:
        # Normal RAG query
        result = rag.answer_query(query, api_key=api_key)
    
    return jsonify(result)

@app.route("/plans", methods=["GET"])
def get_plans():
    """Get all recharge plans"""
    recharge = get_recharge_service()
    plan_type = request.args.get("type", "all")
    
    if plan_type == "prepaid":
        plans = recharge.get_prepaid_plans()
    elif plan_type == "postpaid":
        plans = recharge.get_postpaid_plans()
    elif plan_type == "popular":
        plans = recharge.get_popular_plans()
    else:
        plans = recharge.get_all_plans()
    
    return jsonify({"plans": plans})

@app.route("/plans/<plan_id>", methods=["GET"])
def get_plan_details(plan_id):
    """Get specific plan details"""
    recharge = get_recharge_service()
    plan = recharge.get_plan_by_id(plan_id)
    
    if plan:
        return jsonify({"plan": plan})
    else:
        return jsonify({"error": "Plan not found"}), 404

@app.route("/bills/<mobile>", methods=["GET"])
def get_bills(mobile):
    """Get bills for a mobile number"""
    billing = get_billing_service()
    bills = billing.get_bills(mobile)
    pending = billing.get_pending_bills(mobile)
    
    return jsonify({
        "mobile": mobile,
        "all_bills": bills,
        "pending_bills": pending,
        "total_due": sum(b['amount'] for b in pending)
    })

@app.route("/payments/<mobile>", methods=["GET"])
def get_payments(mobile):
    """Get payment history for a mobile number"""
    billing = get_billing_service()
    payments = billing.get_payment_history(mobile)
    
    return jsonify({
        "mobile": mobile,
        "payments": payments
    })

@app.route("/pay", methods=["POST"])
def make_payment():
    """Process a payment"""
    data = request.json
    mobile = data.get("mobile")
    bill_id = data.get("bill_id")
    amount = data.get("amount")
    payment_method = data.get("payment_method", "UPI")
    
    if not all([mobile, bill_id, amount]):
        return jsonify({"error": "Missing required fields"}), 400
    
    billing = get_billing_service()
    result = billing.make_payment(mobile, bill_id, amount, payment_method)
    
    return jsonify(result)

@app.route("/status", methods=["GET"])
def status():
    rag = get_rag_service()
    return jsonify({
        "status": "ready" if rag.tfidf_matrix is not None else "empty (no data)",
        "doc_count": rag.tfidf_matrix.shape[0] if rag.tfidf_matrix is not None else 0
    })

if __name__ == "__main__":
    # Pre-load services on startup
    print("Initializing RAG Service...")
    get_rag_service()
    
    print("Initializing Billing Service...")
    get_billing_service()
    
    print("Initializing Recharge Service...")
    get_recharge_service()
    
    print("Server starting at http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)


@app.route("/bills/<mobile>", methods=["GET"])
def get_bills(mobile):
    """Get bills for a mobile number"""
    billing = get_billing_service()
    bills = billing.get_bills(mobile)
    pending = billing.get_pending_bills(mobile)
    
    return jsonify({
        "mobile": mobile,
        "all_bills": bills,
        "pending_bills": pending,
        "total_due": sum(b['amount'] for b in pending)
    })

@app.route("/payments/<mobile>", methods=["GET"])
def get_payments(mobile):
    """Get payment history for a mobile number"""
    billing = get_billing_service()
    payments = billing.get_payment_history(mobile)
    
    return jsonify({
        "mobile": mobile,
        "payments": payments
    })

@app.route("/pay", methods=["POST"])
def make_payment():
    """Process a payment"""
    data = request.json
    mobile = data.get("mobile")
    bill_id = data.get("bill_id")
    amount = data.get("amount")
    payment_method = data.get("payment_method", "UPI")
    
    if not all([mobile, bill_id, amount]):
        return jsonify({"error": "Missing required fields"}), 400
    
    billing = get_billing_service()
    result = billing.make_payment(mobile, bill_id, amount, payment_method)
    
    return jsonify(result)

@app.route("/status", methods=["GET"])
def status():
    rag = get_rag_service()
    return jsonify({
        "status": "ready" if rag.tfidf_matrix is not None else "empty (no data)",
        "doc_count": rag.tfidf_matrix.shape[0] if rag.tfidf_matrix is not None else 0
    })

if __name__ == "__main__":
    # Pre-load services on startup
    print("Initializing RAG Service...")
    get_rag_service()
    
    print("Initializing Billing Service...")
    get_billing_service()
    
    print("Server starting at http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)

    print("Initializing RAG Service...")
    get_rag_service()
    print("Server starting at http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
