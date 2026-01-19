import streamlit as st
import langchain_helper
import re

# Page config
st.set_page_config(
    page_title="Restaurant Name Generator",
    page_icon="🍽️",
    layout="centered"
)

st.title("🍴 Restaurant Name Generator")

# Famous cuisines / countries
cuisines = (
    "Indian 🇮🇳",
    "Italian 🇮🇹",
    "Mexican 🇲🇽",
    "Chinese 🇨🇳",
    "Japanese 🇯🇵",
    "Thai 🇹🇭",
    "French 🇫🇷",
    "Spanish 🇪🇸",
    "Greek 🇬🇷",
    "Arabic 🇸🇦",
    "Turkish 🇹🇷",
    "American 🇺🇸",
    "Korean 🇰🇷",
    "Vietnamese 🇻🇳",
    "Mediterranean 🌍",
    "Brazilian 🇧🇷",
    "British 🇬🇧",
    "German 🇩🇪"
)

cuisine = st.sidebar.selectbox("🌎 Pick a Cuisine", cuisines)

if cuisine:
    with st.spinner("✨ Creating a delicious concept..."):
        response = langchain_helper.generate_restaurant_name_and_items(cuisine)

    # ✅ Clean restaurant name
    restaurant_name = response["restaurant_name"].replace('"', '').strip()

    # ✅ Clean & normalize menu items (handles 1., 2., commas, mixed)
    raw_items = response["menu_items"].replace('"', '').strip()

    # Split numbered lists like "1. Item", "2. Item"
    items = re.split(r"\d+\.\s*", raw_items)

    # If not numbered, fallback to comma split
    if len(items) <= 1:
        items = raw_items.split(",")

    # Final clean list
    menu_items = [item.strip() for item in items if item.strip()]

    # Display restaurant name
    st.markdown(
        f"""
        <h2 style="text-align:center; color:#2c3e50;">
            🍽️ {restaurant_name}
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.subheader("📜 Menu")

    for item in menu_items:
        st.markdown(f"• **{item}**")
