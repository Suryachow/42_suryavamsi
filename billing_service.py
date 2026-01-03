import json
import os
from datetime import datetime, timedelta
import random

class BillingService:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.bills_file = os.path.join(data_dir, "user_bills.json")
        self.payments_file = os.path.join(data_dir, "payment_history.json")
        
        # Initialize data files if they don't exist
        if not os.path.exists(self.bills_file):
            self._create_sample_bills()
        if not os.path.exists(self.payments_file):
            self._create_sample_payments()
    
    def _create_sample_bills(self):
        """Create sample billing data"""
        sample_bills = {
            "9811001234": [
                {
                    "bill_id": "BILL001",
                    "mobile": "9811001234",
                    "name": "Rahul Kumar",
                    "plan": "Unlimited 5G - 299",
                    "amount": 299.0,
                    "due_date": (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d"),
                    "status": "pending",
                    "billing_period": "Dec 2025"
                },
                {
                    "bill_id": "BILL002",
                    "mobile": "9811001234",
                    "name": "Rahul Kumar",
                    "plan": "Unlimited 5G - 299",
                    "amount": 299.0,
                    "due_date": "2025-12-10",
                    "status": "paid",
                    "billing_period": "Nov 2025",
                    "paid_date": "2025-12-08"
                }
            ],
            "9876543210": [
                {
                    "bill_id": "BILL003",
                    "mobile": "9989313989",
                    "name": "Suryavamsi",
                    "plan": "Postpaid Plus - 599",
                    "amount": 599.0,
                    "due_date": (datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d"),
                    "status": "pending",
                    "billing_period": "Jan 2026"
                }
            ]
        }
        
        os.makedirs(self.data_dir, exist_ok=True)
        with open(self.bills_file, 'w') as f:
            json.dump(sample_bills, f, indent=2)
    
    def _create_sample_payments(self):
        """Create sample payment history"""
        sample_payments = {
            "9811001234": [
                {
                    "payment_id": "PAY001",
                    "bill_id": "BILL002",
                    "amount": 299.0,
                    "payment_date": "2025-12-08",
                    "payment_method": "UPI",
                    "transaction_id": "TXN202512081234",
                    "status": "success"
                }
            ],
            "9876543210": []
        }
        
        with open(self.payments_file, 'w') as f:
            json.dump(sample_payments, f, indent=2)
    
    def get_bills(self, mobile):
        """Get all bills for a mobile number"""
        try:
            with open(self.bills_file, 'r') as f:
                all_bills = json.load(f)
            return all_bills.get(mobile, [])
        except Exception as e:
            print(f"Error loading bills: {e}")
            return []
    
    def get_pending_bills(self, mobile):
        """Get pending bills for a mobile number"""
        bills = self.get_bills(mobile)
        return [b for b in bills if b['status'] == 'pending']
    
    def get_bill_summary(self, mobile):
        """Get bill summary for AI to use"""
        bills = self.get_bills(mobile)
        pending = [b for b in bills if b['status'] == 'pending']
        
        if not bills:
            return f"No billing information found for mobile number {mobile}."
        
        summary = f"Billing Summary for {mobile}:\n"
        summary += f"Customer Name: {bills[0]['name']}\n"
        summary += f"Current Plan: {bills[0]['plan']}\n\n"
        
        if pending:
            summary += "PENDING BILLS:\n"
            for bill in pending:
                summary += f"- Bill ID: {bill['bill_id']}\n"
                summary += f"  Amount: ₹{bill['amount']}\n"
                summary += f"  Due Date: {bill['due_date']}\n"
                summary += f"  Period: {bill['billing_period']}\n\n"
            
            total_due = sum(b['amount'] for b in pending)
            summary += f"Total Amount Due: ₹{total_due}\n"
        else:
            summary += "No pending bills. All bills are paid.\n"
        
        return summary
    
    def get_payment_history(self, mobile):
        """Get payment history for a mobile number"""
        try:
            with open(self.payments_file, 'r') as f:
                all_payments = json.load(f)
            return all_payments.get(mobile, [])
        except Exception as e:
            print(f"Error loading payments: {e}")
            return []
    
    def make_payment(self, mobile, bill_id, amount, payment_method="UPI"):
        """Process a payment"""
        try:
            # Load bills
            with open(self.bills_file, 'r') as f:
                all_bills = json.load(f)
            
            # Find and update bill
            if mobile in all_bills:
                for bill in all_bills[mobile]:
                    if bill['bill_id'] == bill_id:
                        bill['status'] = 'paid'
                        bill['paid_date'] = datetime.now().strftime("%Y-%m-%d")
                        break
                
                # Save updated bills
                with open(self.bills_file, 'w') as f:
                    json.dump(all_bills, f, indent=2)
            
            # Add payment record
            with open(self.payments_file, 'r') as f:
                all_payments = json.load(f)
            
            if mobile not in all_payments:
                all_payments[mobile] = []
            
            payment = {
                "payment_id": f"PAY{random.randint(1000, 9999)}",
                "bill_id": bill_id,
                "amount": amount,
                "payment_date": datetime.now().strftime("%Y-%m-%d"),
                "payment_method": payment_method,
                "transaction_id": f"TXN{datetime.now().strftime('%Y%m%d%H%M%S')}",
                "status": "success"
            }
            
            all_payments[mobile].append(payment)
            
            with open(self.payments_file, 'w') as f:
                json.dump(all_payments, f, indent=2)
            
            return {
                "success": True,
                "message": "Payment successful",
                "payment": payment
            }
        
        except Exception as e:
            return {
                "success": False,
                "message": f"Payment failed: {str(e)}"
            }
    
    def search_bills(self, query):
        """Search bills based on query for RAG integration"""
        try:
            # Extract mobile number from query if present
            import re
            mobile_match = re.search(r'\b\d{10}\b', query)
            
            if mobile_match:
                mobile = mobile_match.group()
                return self.get_bill_summary(mobile)
            else:
                return "Please provide a valid 10-digit mobile number to check bills."
        
        except Exception as e:
            return f"Error searching bills: {str(e)}"
