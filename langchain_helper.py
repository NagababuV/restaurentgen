from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

# Make sure OPENAI_API_KEY is set in environment
# export OPENAI_API_KEY="your-api-key"

llm = OpenAI(temperature=0.7)

def generate_restaurant_name_and_items(cuisine):
    # Prompt for restaurant name
    name_prompt = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} cuisine. Suggest a fancy and unique restaurant name."
    )

    restaurant_name = llm.invoke(
        name_prompt.format(cuisine=cuisine)
    ).strip()

    # Prompt for menu items
    items_prompt = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest 8 to 10 popular menu items for {restaurant_name}. Return as a comma separated list."
    )

    menu_items = llm.invoke(
        items_prompt.format(restaurant_name=restaurant_name)
    ).strip()

    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
