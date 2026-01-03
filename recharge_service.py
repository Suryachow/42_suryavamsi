import json
import os
from datetime import datetime, timedelta

class RechargeService:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.plans_file = os.path.join(data_dir, "recharge_plans.json")
        
        # Initialize plans if they don't exist
        if not os.path.exists(self.plans_file):
            self._create_recharge_plans()
    
    def _create_recharge_plans(self):
        """Create realistic telecom recharge plans"""
        plans = {
            "prepaid": {
                "unlimited": [
                    {
                        "plan_id": "UNL299",
                        "name": "Unlimited 5G",
                        "price": 299,
                        "validity": "28 days",
                        "data": "2GB/day",
                        "unlimited_5g": True,
                        "calls": "Unlimited",
                        "sms": "100 SMS/day",
                        "ott": ["Disney+ Hotstar Mobile"],
                        "popular": True
                    },
                    {
                        "plan_id": "UNL399",
                        "name": "Unlimited Plus",
                        "price": 399,
                        "validity": "28 days",
                        "data": "2.5GB/day",
                        "unlimited_5g": True,
                        "calls": "Unlimited",
                        "sms": "100 SMS/day",
                        "ott": ["Disney+ Hotstar", "Amazon Prime Lite"],
                        "popular": False
                    },
                    {
                        "plan_id": "UNL666",
                        "name": "Unlimited Premium",
                        "price": 666,
                        "validity": "56 days",
                        "data": "3GB/day",
                        "unlimited_5g": True,
                        "calls": "Unlimited",
                        "sms": "100 SMS/day",
                        "ott": ["Netflix Basic", "Disney+ Hotstar", "Amazon Prime"],
                        "popular": True
                    },
                    {
                        "plan_id": "UNL839",
                        "name": "Unlimited Ultra",
                        "price": 839,
                        "validity": "84 days",
                        "data": "2GB/day",
                        "unlimited_5g": True,
                        "calls": "Unlimited",
                        "sms": "100 SMS/day",
                        "ott": ["Disney+ Hotstar", "Amazon Prime"],
                        "popular": False
                    }
                ],
                "data_only": [
                    {
                        "plan_id": "DATA99",
                        "name": "Data Booster",
                        "price": 99,
                        "validity": "7 days",
                        "data": "6GB",
                        "unlimited_5g": False,
                        "calls": "None",
                        "sms": "None",
                        "ott": [],
                        "popular": False
                    },
                    {
                        "plan_id": "DATA181",
                        "name": "Data Power",
                        "price": 181,
                        "validity": "28 days",
                        "data": "15GB",
                        "unlimited_5g": False,
                        "calls": "None",
                        "sms": "None",
                        "ott": [],
                        "popular": False
                    }
                ],
                "long_validity": [
                    {
                        "plan_id": "LV1799",
                        "name": "Annual Unlimited",
                        "price": 1799,
                        "validity": "365 days",
                        "data": "2GB/day",
                        "unlimited_5g": True,
                        "calls": "Unlimited",
                        "sms": "100 SMS/day",
                        "ott": ["Disney+ Hotstar"],
                        "popular": True
                    },
                    {
                        "plan_id": "LV2999",
                        "name": "Annual Premium",
                        "price": 2999,
                        "validity": "365 days",
                        "data": "2.5GB/day",
                        "unlimited_5g": True,
                        "calls": "Unlimited",
                        "sms": "100 SMS/day",
                        "ott": ["Netflix", "Disney+ Hotstar", "Amazon Prime"],
                        "popular": False
                    }
                ]
            },
            "postpaid": [
                {
                    "plan_id": "POST399",
                    "name": "Postpaid Basic",
                    "price": 399,
                    "data": "40GB/month",
                    "rollover": True,
                    "calls": "Unlimited",
                    "sms": "100 SMS/day",
                    "connections": 1,
                    "ott": [],
                    "popular": False
                },
                {
                    "plan_id": "POST599",
                    "name": "Postpaid Plus",
                    "price": 599,
                    "data": "75GB/month",
                    "rollover": True,
                    "calls": "Unlimited",
                    "sms": "100 SMS/day",
                    "connections": 2,
                    "ott": ["Netflix Basic", "Amazon Prime"],
                    "popular": True
                },
                {
                    "plan_id": "POST999",
                    "name": "Postpaid Premium",
                    "price": 999,
                    "data": "150GB/month",
                    "rollover": True,
                    "calls": "Unlimited",
                    "sms": "Unlimited",
                    "connections": 3,
                    "ott": ["Netflix Standard", "Disney+ Hotstar", "Amazon Prime"],
                    "popular": False
                },
                {
                    "plan_id": "POST1599",
                    "name": "Postpaid Platinum",
                    "price": 1599,
                    "data": "200GB/month",
                    "rollover": True,
                    "calls": "Unlimited",
                    "sms": "Unlimited",
                    "connections": 4,
                    "ott": ["Netflix Premium", "Disney+ Hotstar", "Amazon Prime", "YouTube Premium"],
                    "popular": True
                }
            ]
        }
        
        os.makedirs(self.data_dir, exist_ok=True)
        with open(self.plans_file, 'w') as f:
            json.dump(plans, f, indent=2)
    
    def get_all_plans(self):
        """Get all available plans"""
        try:
            with open(self.plans_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading plans: {e}")
            return {}
    
    def get_prepaid_plans(self, category=None):
        """Get prepaid plans, optionally filtered by category"""
        plans = self.get_all_plans()
        prepaid = plans.get("prepaid", {})
        
        if category:
            return prepaid.get(category, [])
        
        # Return all prepaid plans combined
        all_prepaid = []
        for cat_plans in prepaid.values():
            all_prepaid.extend(cat_plans)
        return all_prepaid
    
    def get_postpaid_plans(self):
        """Get postpaid plans"""
        plans = self.get_all_plans()
        return plans.get("postpaid", [])
    
    def get_popular_plans(self):
        """Get popular/recommended plans"""
        all_plans = self.get_all_plans()
        popular = []
        
        # Get popular prepaid
        for category in all_plans.get("prepaid", {}).values():
            popular.extend([p for p in category if p.get("popular")])
        
        # Get popular postpaid
        popular.extend([p for p in all_plans.get("postpaid", []) if p.get("popular")])
        
        return popular
    
    def search_plans(self, query):
        """Search plans based on query for AI integration"""
        query_lower = query.lower()
        
        # Detect intent
        is_prepaid = any(word in query_lower for word in ["prepaid", "recharge", "topup", "top up"])
        is_postpaid = any(word in query_lower for word in ["postpaid", "bill", "monthly"])
        is_data_only = any(word in query_lower for word in ["data only", "internet only"])
        is_long_validity = any(word in query_lower for word in ["annual", "yearly", "long term", "365"])
        
        result = "📱 **Available Recharge Plans**\n\n"
        
        if is_data_only:
            plans = self.get_prepaid_plans("data_only")
            result += "🌐 **Data Only Plans:**\n"
            for plan in plans:
                result += f"• **{plan['name']}** - ₹{plan['price']}\n"
                result += f"  Data: {plan['data']}, Validity: {plan['validity']}\n\n"
        
        elif is_long_validity:
            plans = self.get_prepaid_plans("long_validity")
            result += "📅 **Long Validity Plans:**\n"
            for plan in plans:
                result += f"• **{plan['name']}** - ₹{plan['price']}\n"
                result += f"  Data: {plan['data']}, Validity: {plan['validity']}\n"
                if plan.get('ott'):
                    result += f"  OTT: {', '.join(plan['ott'])}\n"
                result += "\n"
        
        elif is_postpaid:
            plans = self.get_postpaid_plans()
            result += "💼 **Postpaid Plans:**\n"
            for plan in plans:
                result += f"• **{plan['name']}** - ₹{plan['price']}/month\n"
                result += f"  Data: {plan['data']}, Connections: {plan['connections']}\n"
                if plan.get('ott'):
                    result += f"  OTT: {', '.join(plan['ott'])}\n"
                if plan.get('popular'):
                    result += f"  ⭐ Popular Choice\n"
                result += "\n"
        
        else:  # Default: Show popular prepaid unlimited plans
            plans = self.get_prepaid_plans("unlimited")
            result += "🔥 **Popular Unlimited Plans:**\n"
            for plan in plans:
                if plan.get('popular'):
                    result += f"• **{plan['name']}** - ₹{plan['price']} ⭐\n"
                else:
                    result += f"• **{plan['name']}** - ₹{plan['price']}\n"
                result += f"  Data: {plan['data']}, Validity: {plan['validity']}\n"
                result += f"  5G: {'Yes' if plan.get('unlimited_5g') else 'No'}\n"
                if plan.get('ott'):
                    result += f"  OTT: {', '.join(plan['ott'])}\n"
                result += "\n"
        
        return result
    
    def get_plan_by_id(self, plan_id):
        """Get a specific plan by ID"""
        all_plans = self.get_all_plans()
        
        # Search in prepaid
        for category in all_plans.get("prepaid", {}).values():
            for plan in category:
                if plan.get("plan_id") == plan_id:
                    return plan
        
        # Search in postpaid
        for plan in all_plans.get("postpaid", []):
            if plan.get("plan_id") == plan_id:
                return plan
        
        return None
