import streamlit as st
import pandas as pd
import datetime

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Royal Vine - Sales & Inventory System",
    page_icon="🌿",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1b4332;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1rem;
        color: #40916c;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# INITIAL SAMPLE DATA FROM PROVIDED IMAGE
# ==========================================
INITIAL_INVENTORY = [
    {"Item": "Mangoes TA", "Quantity": 41, "Price_BWP": 120.0, "Cost_BWP": 70.0},
    {"Item": "Mangoes Keitt", "Quantity": 40, "Price_BWP": 120.0, "Cost_BWP": 70.0},
    {"Item": "Skyrocket", "Quantity": 4, "Price_BWP": 180.0, "Cost_BWP": 110.0},
    {"Item": "Almonds", "Quantity": 1, "Price_BWP": 180.0, "Cost_BWP": 110.0},
    {"Item": "Bamboo 10L", "Quantity": 9, "Price_BWP": 150.0, "Cost_BWP": 90.0},
    {"Item": "Bamboo 5L", "Quantity": 14, "Price_BWP": 100.0, "Cost_BWP": 60.0},
    {"Item": "Pear", "Quantity": 29, "Price_BWP": 175.0, "Cost_BWP": 100.0},
    {"Item": "Apples Anna", "Quantity": 0, "Price_BWP": 175.0, "Cost_BWP": 100.0},
    {"Item": "Apples Golden Crest", "Quantity": 10, "Price_BWP": 175.0, "Cost_BWP": 100.0},
    {"Item": "Apples Gran Smth", "Quantity": 10, "Price_BWP": 175.0, "Cost_BWP": 100.0},
    {"Item": "Nectarine", "Quantity": 5, "Price_BWP": 180.0, "Cost_BWP": 110.0},
    {"Item": "Fig", "Quantity": 6, "Price_BWP": 160.0, "Cost_BWP": 95.0},
    {"Item": "Peach", "Quantity": 7, "Price_BWP": 180.0, "Cost_BWP": 110.0},
    {"Item": "Blueberries", "Quantity": 50, "Price_BWP": 140.0, "Cost_BWP": 80.0},
    {"Item": "Kiwi Male", "Quantity": 5, "Price_BWP": 140.0, "Cost_BWP": 80.0},
    {"Item": "Kiwi HayW female", "Quantity": 5, "Price_BWP": 140.0, "Cost_BWP": 80.0},
    {"Item": "Avocado", "Quantity": 20, "Price_BWP": 250.0, "Cost_BWP": 150.0},
    {"Item": "Coffee", "Quantity": 8, "Price_BWP": 150.0, "Cost_BWP": 90.0},
    {"Item": "Litchi", "Quantity": 4, "Price_BWP": 170.0, "Cost_BWP": 100.0},
    {"Item": "Strawberry", "Quantity": 10, "Price_BWP": 60.0, "Cost_BWP": 35.0},
    {"Item": "Grapes Crimson s", "Quantity": 5, "Price_BWP": 150.0, "Cost_BWP": 90.0},
    {"Item": "Guava Lucknow w", "Quantity": 8, "Price_BWP": 150.0, "Cost_BWP": 90.0},
    {"Item": "Banana", "Quantity": 15, "Price_BWP": 100.0, "Cost_BWP": 60.0},
    {"Item": "Olives Mission", "Quantity": 5, "Price_BWP": 180.0, "Cost_BWP": 105.0},
    {"Item": "Olives Frantoio", "Quantity": 6, "Price_BWP": 180.0, "Cost_BWP": 105.0},
    {"Item": "Grapes:Red Globe", "Quantity": 7, "Price_BWP": 150.0, "Cost_BWP": 90.0},
    {"Item": "Pomegranate", "Quantity": 8, "Price_BWP": 150.0, "Cost_BWP": 90.0},
    {"Item": "Macadamia", "Quantity": 8, "Price_BWP": 180.0, "Cost_BWP": 110.0},
    {"Item": "Walnut", "Quantity": 22, "Price_BWP": 180.0, "Cost_BWP": 110.0},
    {"Item": "Cocos Palm 10L", "Quantity": 9, "Price_BWP": 240.0, "Cost_BWP": 140.0},
    {"Item": "Revoluta 5L", "Quantity": 8, "Price_BWP": 80.0, "Cost_BWP": 45.0},
    {"Item": "Royal Palm", "Quantity": 89, "Price_BWP": 240.0, "Cost_BWP": 140.0},
    {"Item": "Lapin Cherry", "Quantity": 10, "Price_BWP": 400.0, "Cost_BWP": 250.0},
    {"Item": "Cupressus Goldcrest", "Quantity": 8, "Price_BWP": 220.0, "Cost_BWP": 130.0},
    {"Item": "Plum", "Quantity": 5, "Price_BWP": 180.0, "Cost_BWP": 105.0}
]

PAYMENT_METHODS = [
    "Cash",
    "Pay2Cell (76097648)",
    "Pay2Cell (74615100)",
    "Orange Money (72707255)",
    "Orange Money (72796888)",
    "MyZaka (74615100)",
    "MyZaka (76097648)",
    "Other"
]

# Initialize Session States
if "inventory" not in st.session_state:
    st.session_state.inventory = pd.DataFrame(INITIAL_INVENTORY)

# Cart state for multi-item checkout
if "pos_cart" not in st.session_state:
    st.session_state.pos_cart = []

if "sales_history" not in st.session_state:
    # Pre-populating sample sales data across different weeks for demonstration
    sample_sales = [
        {"Date": datetime.date(2026, 11, 2), "Item": "Mangoes TA", "Quantity": 5, "Price_BWP": 120.0, "Total_BWP": 600.0, "Cost_BWP": 350.0, "Profit_BWP": 250.0, "Payment_Method": "Pay2Cell (76097648)"},
        {"Date": datetime.date(2026, 11, 6), "Item": "Royal Palm", "Quantity": 2, "Price_BWP": 240.0, "Total_BWP": 480.0, "Cost_BWP": 280.0, "Profit_BWP": 200.0, "Payment_Method": "Orange Money (72707255)"},
        {"Date": datetime.date(2026, 11, 10), "Item": "Blueberries", "Quantity": 4, "Price_BWP": 140.0, "Total_BWP": 560.0, "Cost_BWP": 320.0, "Profit_BWP": 240.0, "Payment_Method": "Cash"},
        {"Date": datetime.date(2026, 11, 18), "Item": "Lapin Cherry", "Quantity": 1, "Price_BWP": 400.0, "Total_BWP": 400.0, "Cost_BWP": 250.0, "Profit_BWP": 150.0, "Payment_Method": "MyZaka (74615100)"},
        {"Date": datetime.date(2026, 11, 25), "Item": "Avocado", "Quantity": 3, "Price_BWP": 250.0, "Total_BWP": 750.0, "Cost_BWP": 450.0, "Profit_BWP": 300.0, "Payment_Method": "Cash"}
    ]
    st.session_state.sales_history = pd.DataFrame(sample_sales)

if "refills" not in st.session_state:
    st.session_state.refills = pd.DataFrame(columns=["Date", "Item", "Quantity_Added", "Unit_Cost_BWP", "Notes"])

if "expenses" not in st.session_state:
    sample_expenses = [
        {"Date": datetime.date(2026, 11, 3), "Category": "Transport / Delivery", "Amount_BWP": 250.0, "Notes": "Stock transport from supplier"},
        {"Date": datetime.date(2026, 11, 15), "Category": "Fertilizer / Soil", "Amount_BWP": 180.0, "Notes": "Organic potting soil"}
    ]
    st.session_state.expenses = pd.DataFrame(sample_expenses)

# ==========================================
# MODULE 1: RECORD SALE (MULTI-ITEM CART)
# ==========================================
if choice == "🛒 Record Sale":
    st.subheader("Record New Sale (Multi-Item Order)")
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown("### 1. Add Varieties to Order Cart")
        inv_df = st.session_state.inventory
        item_options = inv_df["Item"].tolist()
        
        c_item, c_qty, c_btn = st.columns([3, 2, 2])
        with c_item:
            selected_item = st.selectbox("Select Item Variety", item_options)
            item_row = inv_df[inv_df["Item"] == selected_item].iloc[0]
            current_stock = int(item_row["Quantity"])
            item_price = float(item_row["Price_BWP"])
            item_cost = float(item_row["Cost_BWP"])
            st.caption(f"Stock: **{current_stock}** | Unit Price: **BWP {item_price:.2f}**")
            
        with c_qty:
            sale_qty = st.number_input("Quantity", min_value=1, max_value=max(1, current_stock), value=1, step=1)
            
        with c_btn:
            st.write("") # Alignment spacing
            st.write("")
            if st.button("➕ Add to Cart", use_container_width=True):
                if current_stock < sale_qty:
                    st.error("Insufficient stock!")
                else:
                    # Check if item already in cart
                    existing_item = next((item for item in st.session_state.pos_cart if item["Item"] == selected_item), None)
                    if existing_item:
                        if (existing_item["Quantity"] + sale_qty) > current_stock:
                            st.error(f"Cannot exceed available stock ({current_stock}).")
                        else:
                            existing_item["Quantity"] += sale_qty
                            existing_item["Total_Price"] = existing_item["Quantity"] * item_price
                            existing_item["Total_Cost"] = existing_item["Quantity"] * item_cost
                            st.success(f"Updated {selected_item} quantity in cart!")
                    else:
                        st.session_state.pos_cart.append({
                            "Item": selected_item,
                            "Quantity": sale_qty,
                            "Price_BWP": item_price,
                            "Cost_BWP": item_cost,
                            "Total_Price": sale_qty * item_price,
                            "Total_Cost": sale_qty * item_cost
                        })
                        st.success(f"Added {selected_item} to cart!")

    with col2:
        st.markdown("### 2. Order Summary & Checkout")
        sale_date = st.date_input("Sale Date", datetime.date.today())
        payment_method = st.selectbox("Payment Method", PAYMENT_METHODS)
        
        if len(st.session_state.pos_cart) == 0:
            st.info("🛒 Your order cart is empty. Add items from the left to start.")
        else:
            cart_df = pd.DataFrame(st.session_state.pos_cart)
            st.dataframe(
                cart_df[["Item", "Quantity", "Price_BWP", "Total_Price"]],
                use_container_width=True,
                column_config={
                    "Price_BWP": st.column_config.NumberColumn("Unit Price", format="BWP %.2f"),
                    "Total_Price": st.column_config.NumberColumn("Subtotal", format="BWP %.2f"),
                }
            )
            
            cart_total_price = cart_df["Total_Price"].sum()
            cart_total_cost = cart_df["Total_Cost"].sum()
            cart_profit = cart_total_price - cart_total_cost
            
            st.markdown(f"**Total Revenue:** `BWP {cart_total_price:.2f}`")
            st.markdown(f"**Estimated Margin:** `BWP {cart_profit:.2f}`")
            
            c_clear, c_checkout = st.columns([1, 2])
            with c_clear:
                if st.button("🗑️ Clear Cart", use_container_width=True):
                    st.session_state.pos_cart = []
                    st.rerun()
                    
            with c_checkout:
                if st.button("✅ Complete Order", type="primary", use_container_width=True):
                    # Process each item in cart
                    for cart_item in st.session_state.pos_cart:
                        # Deduct inventory
                        st.session_state.inventory.loc[
                            st.session_state.inventory["Item"] == cart_item["Item"], "Quantity"
                        ] -= cart_item["Quantity"]
                        
                        # Append to sales history
                        new_sale = {
                            "Date": sale_date,
                            "Item": cart_item["Item"],
                            "Quantity": cart_item["Quantity"],
                            "Price_BWP": cart_item["Price_BWP"],
                            "Total_BWP": cart_item["Total_Price"],
                            "Cost_BWP": cart_item["Total_Cost"],
                            "Profit_BWP": cart_item["Total_Price"] - cart_item["Total_Cost"],
                            "Payment_Method": payment_method
                        }
                        st.session_state.sales_history = pd.concat(
                            [st.session_state.sales_history, pd.DataFrame([new_sale])], 
                            ignore_index=True
                        )
                    
                    st.session_state.pos_cart = []
                    st.success(f"Order processed successfully! Recorded {len(cart_df)} line items under {payment_method}.")
                    st.rerun()

# ==========================================
# MODULE 2: INVENTORY LIST
# ==========================================
elif choice == "📦 Inventory List":
    st.subheader("Current Stock Inventory")
    
    col_search, col_add = st.columns([3, 1])
    with col_search:
        search_query = st.text_input("Search Plant or Product", "")
    
    inv_df = st.session_state.inventory.copy()
    if search_query:
        inv_df = inv_df[inv_df["Item"].str.contains(search_query, case=False, na=False)]
        
    # Highlight low stock items
    st.dataframe(
        inv_df.style.map(
            lambda val: 'background-color: #ffcdd2; color: #b71c1c; font-weight: bold;' if isinstance(val, (int, float)) and val <= 3 else '', 
            subset=['Quantity']
        ),
        use_container_width=True,
        column_config={
            "Price_BWP": st.column_config.NumberColumn("Selling Price (BWP)", format="BWP %.2f"),
            "Cost_BWP": st.column_config.NumberColumn("Unit Cost (BWP)", format="BWP %.2f"),
        }
    )
    
    st.markdown("### Add New SKU / Plant Variety")
    with st.form("add_new_sku_form"):
        f_col1, f_col2, f_col3, f_col4 = st.columns(4)
        new_item = f_col1.text_input("Item Name")
        new_qty = f_col2.number_input("Starting Quantity", min_value=0, value=10)
        new_price = f_col3.number_input("Selling Price (BWP)", min_value=0.0, value=150.0, step=10.0)
        new_cost = f_col4.number_input("Unit Cost (BWP)", min_value=0.0, value=90.0, step=10.0)
        
        submit_sku = st.form_submit_button("Add SKU to Catalog")
        if submit_sku:
            if new_item in st.session_state.inventory["Item"].values:
                st.error("Item already exists in catalog!")
            elif new_item.strip() == "":
                st.warning("Please provide a valid item name.")
            else:
                new_row = {"Item": new_item.strip(), "Quantity": new_qty, "Price_BWP": new_price, "Cost_BWP": new_cost}
                st.session_state.inventory = pd.concat([st.session_state.inventory, pd.DataFrame([new_row])], ignore_index=True)
                st.success(f"Added {new_item} to catalog!")
                st.rerun()

# ==========================================
# MODULE 3: STOCK REFILL
# ==========================================
elif choice == "🚚 Stock Refill":
    st.subheader("Record Stock Refills & Replenishments")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        refill_date = st.date_input("Refill Date", datetime.date.today())
        item_to_refill = st.selectbox("Item to Refill", st.session_state.inventory["Item"].tolist())
        qty_to_add = st.number_input("Quantity Received / Added", min_value=1, value=10)
        unit_cost = st.number_input("Unit Purchase Cost (BWP)", min_value=0.0, value=80.0, step=5.0)
        refill_notes = st.text_input("Notes / Supplier Reference", "Batch delivery")
        
        if st.button("📥 Process Stock Refill", type="primary"):
            # Update inventory quantity
            st.session_state.inventory.loc[st.session_state.inventory["Item"] == item_to_refill, "Quantity"] += qty_to_add
            st.session_state.inventory.loc[st.session_state.inventory["Item"] == item_to_refill, "Cost_BWP"] = unit_cost
            
            # Log refill entry
            refill_entry = {
                "Date": refill_date,
                "Item": item_to_refill,
                "Quantity_Added": qty_to_add,
                "Unit_Cost_BWP": unit_cost,
                "Notes": refill_notes
            }
            st.session_state.refills = pd.concat([st.session_state.refills, pd.DataFrame([refill_entry])], ignore_index=True)
            st.success(f"Successfully added {qty_to_add} units of {item_to_refill} to stock!")

    with col2:
        st.markdown("### Recent Refill Logs")
        if not st.session_state.refills.empty:
            st.dataframe(st.session_state.refills.tail(5), use_container_width=True)
        else:
            st.info("No stock refills logged yet.")

# ==========================================
# MODULE 4: EXPENSES & OPERATIONAL COSTS
# ==========================================
elif choice == "💸 Expenses & Operational Costs":
    st.subheader("Capture Operational Costs & Business Expenses")
    st.caption("Track overheads like transport, soil, pots, utilities, and wages to calculate true Net Profit.")
    
    col_f, col_t = st.columns([1, 2])
    
    with col_f:
        exp_date = st.date_input("Expense Date", datetime.date.today())
        exp_category = st.selectbox("Expense Category", ["Transport / Freight", "Soil & Fertilizers", "Pots & Containers", "Labour & Wages", "Utilities & Water", "Marketing", "Other"])
        exp_amount = st.number_input("Amount (BWP)", min_value=0.0, value=100.0, step=10.0)
        exp_notes = st.text_input("Expense Description", "Transport cost for seedlings")
        
        if st.button("💾 Record Expense"):
            new_exp = {
                "Date": exp_date,
                "Category": exp_category,
                "Amount_BWP": exp_amount,
                "Notes": exp_notes
            }
            st.session_state.expenses = pd.concat([st.session_state.expenses, pd.DataFrame([new_exp])], ignore_index=True)
            st.success("Expense recorded successfully!")
            
    with col_t:
        st.markdown("### Expense Ledger")
        if not st.session_state.expenses.empty:
            st.dataframe(st.session_state.expenses, use_container_width=True)
            total_exp = st.session_state.expenses["Amount_BWP"].sum()
            st.metric("Total Operational Costs Recorded", f"BWP {total_exp:.2f}")
        else:
            st.info("No expenses recorded yet.")

# ==========================================
# MODULE 5: WEEKLY & MONTHLY INSIGHTS
# ==========================================
elif choice == "📊 Weekly & Monthly Insights":
    st.subheader("Sales & Profit Analytics (Weekly & Monthly Breakdown)")
    
    sales_df = st.session_state.sales_history.copy()
    exp_df = st.session_state.expenses.copy()
    
    if sales_df.empty:
        st.warning("No sales data recorded yet to generate analytics.")
    else:
        # Date & Week Conversions
        sales_df["Date"] = pd.to_datetime(sales_df["Date"])
        sales_df["Day_of_Month"] = sales_df["Date"].dt.day
        
        # Categorize into Week 1, Week 2, Week 3, Week 4
        def assign_week(day):
            if day <= 7:
                return "Week 1 (1-7)"
            elif day <= 14:
                return "Week 2 (8-14)"
            elif day <= 21:
                return "Week 3 (15-21)"
            else:
                return "Week 4+ (22-End)"
                
        sales_df["Week_Period"] = sales_df["Day_of_Month"].apply(assign_week)
        
        total_rev = sales_df["Total_BWP"].sum()
        total_cogs = sales_df["Cost_BWP"].sum()
        gross_profit = sales_df["Profit_BWP"].sum()
        total_overhead = exp_df["Amount_BWP"].sum() if not exp_df.empty else 0.0
        net_profit = gross_profit - total_overhead
        
        # Executive Summary Metrics
        m1, m2, m3, m4, m5 = st.columns(5)
        m1.metric("Total Revenue", f"BWP {total_rev:.2f}")
        m2.metric("Gross Profit", f"BWP {gross_profit:.2f}")
        m3.metric("Op Expenses", f"BWP {total_overhead:.2f}")
        m4.metric("Net Profit", f"BWP {net_profit:.2f}")
        m5.metric("Total Units Sold", f"{sales_df['Quantity'].sum()}")
        
        st.divider()
        
        # Weekly Sales Summary
        st.markdown("### 📅 Weekly Sales Breakdown (Week 1, 2, 3, 4)")
        weekly_summary = sales_df.groupby("Week_Period").agg(
            Revenue_BWP=("Total_BWP", "sum"),
            Gross_Profit_BWP=("Profit_BWP", "sum"),
            Units_Sold=("Quantity", "sum"),
            Orders=("Item", "count")
        ).reset_index()
        
        col_w1, col_w2 = st.columns([2, 1])
        with col_w1:
            st.bar_chart(weekly_summary.set_index("Week_Period")[["Revenue_BWP", "Gross_Profit_BWP"]])
        with col_w2:
            st.dataframe(weekly_summary, use_container_width=True)
            
        st.divider()
        
        # Payment Method Breakdown
        st.markdown("### 💳 Revenue by Payment Channel")
        payment_summary = sales_df.groupby("Payment_Method")["Total_BWP"].sum().reset_index()
        
        cp1, cp2 = st.columns([1, 1])
        with cp1:
            st.dataframe(payment_summary, use_container_width=True)
        with cp2:
            st.bar_chart(payment_summary.set_index("Payment_Method"))
            
        st.divider()
        
        # Top Selling Items
        st.markdown("### 🏆 Top Performing Plant Varieties")
        top_items = sales_df.groupby("Item").agg(
            Units_Sold=("Quantity", "sum"),
            Total_Revenue_BWP=("Total_BWP", "sum")
        ).sort_values(by="Total_Revenue_BWP", ascending=False).reset_index()
        st.dataframe(top_items, use_container_width=True)

# ==========================================
# MODULE 6: TRANSACTION HISTORY
# ==========================================
elif choice == "📜 Transaction History":
    st.subheader("Sales Ledger & Log History")
    st.dataframe(st.session_state.sales_history, use_container_width=True)
    
    # Download option
    csv_data = st.session_state.sales_history.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Export Sales History (CSV)",
        data=csv_data,
        file_name="royal_vine_sales_history.csv",
        mime="text/csv"
    )

# ==========================================
# MODULE 7: GITHUB & CLOUD DEPLOYMENT GUIDE
# ==========================================
elif choice == "🚀 Deploy to GitHub & Streamlit":
    st.subheader("🚀 Step-by-Step GitHub & Free Cloud Hosting Guide")
    st.caption("Publish Royal Vine Sales & Inventory online so your team can access it from any phone or computer.")
    
    tab1, tab2, tab3 = st.tabs(["1️⃣ Prepare Project Files", "2️⃣ Push to GitHub", "3️⃣ Deploy on Streamlit Cloud"])
    
    with tab1:
        st.markdown("### Step 1: Create your local files")
        st.markdown("Create a folder on your computer named `royal-vine-app` with these 2 files:")
        
        st.markdown("**1. `requirements.txt`** (Tells Streamlit Cloud what libraries to install)")
        st.code("""streamlit>=1.30.0
pandas>=2.0.0""", language="text")
        
        st.markdown("**2. `app.py`** (The main Python application script)")
        st.info("Copy all code from this app into `app.py`.")
        
    with tab2:
        st.markdown("### Step 2: Upload to GitHub")
        st.markdown("""
        1. Go to **[GitHub.com](https://github.com)** and log in (or create a free account).
        2. Click the **`+`** icon in the top right corner and select **New repository**.
        3. Name your repository **`royal-vine-inventory`**.
        4. Choose **Public** (required for free Streamlit hosting) or **Private** (if you have Streamlit Community Team).
        5. Click **Create repository**.
        6. Upload your `app.py` and `requirements.txt` files directly on GitHub by clicking **Uploading an existing file**.
        """)
        
    with tab3:
        st.markdown("### Step 3: Launch Live App on Streamlit Cloud")
        st.markdown("""
        1. Visit **[share.streamlit.io](https://share.streamlit.io)** and sign in with your GitHub account.
        2. Click **Create app** -> **I already have an app**.
        3. Fill in the details:
           - **Repository:** `your-github-username/royal-vine-inventory`
           - **Branch:** `main`
           - **Main file path:** `app.py`
        4. Click **Deploy!** 🚀
        
        Within 1-2 minutes, your web application will be live at a custom URL (e.g., `royal-vine.streamlit.app`) that works on phones, tablets, and laptops!
        """)
