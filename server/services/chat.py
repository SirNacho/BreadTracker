import os
import json
import asyncio
from typing import Dict, List
from dotenv import load_dotenv
from openai import AsyncOpenAI
from google import genai
from google.genai import types

load_dotenv()

SYSTEM_PROMPT = """
You are a grocery data normalization expert. Your task is to take a specific search term and its corresponding list of product SKUs and group them into logical, functional categories.

### Input Format
You will receive the search term and a list of product titles.
Example: 
Search Term: "oreo"
SKUs: ["Oreo Chocolate Sandwich Cookies 14.3oz", "Oreo Cookies 20ct", "Oreo Single Snack Pack", "Nabisco Oreo Family Size"]

### Categorization Rules
1. Functional Equivalence: Group items if an average shopper would consider them interchangeable for a single use case.
2. Specificity: 
   - If the search term is generic (e.g., "apples"), group different varieties (e.g., Gala, Fuji) into the same category.
   - If the search term is specific (e.g., "Gala apples"), keep that variety in its own category and separate it from other varieties.
3. Size/Format: Separate "Single/Snack Packs" from "Standard/Medium" sizes, and separate "Bulk/Wholesale" sizes from both. They serve different use cases.
4. Organic vs. Non-Organic: Never group organic items with non-organic items.
5. Branding: Only create brand-specific categories if the search term explicitly mentions a brand. Otherwise, group across different brands (e.g., Store Brand Milk and Name Brand Milk go together).
6. Naming: Create a concise, descriptive category name (e.g., "Standard Size Chocolate Sandwich Cookies").

### Output Format
Return ONLY a valid JSON object. No prose, no markdown code blocks, no explanations.
Structure: Dict[str, List[str]]
Example:
{
  "Standard & Family Size Oreo Cookies": ["Oreo Chocolate Sandwich Cookies 14.3oz", "Nabisco Oreo Family Size"],
  "Snack Sized Oreo Packs": ["Oreo Cookies 20ct", "Oreo Single Snack Pack"]
}
"""

async def categorize_groceries(grocery_names: Dict[str, List[str]]) -> Dict[str, Dict[str, List[str]]]:
    client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    async def categorize_single_grocery(grocery: str, skus: List[str]):
        try:
            response = await client.chat.completions.create(
                model="gpt-5-nano",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"Search Term: \"{grocery}\"\nSKUs: {json.dumps(skus)}"}
                ],
                response_format={"type": "json_object"}
            )
            
            content = response.choices[0].message.content
            return grocery, json.loads(content)
            
        except Exception as e:
            print(f"Error processing {grocery}: {e}")
            return grocery, {"Error": ["Could not categorize"]}
    
    tasks = [categorize_single_grocery(g, s) for g, s in grocery_names.items()]
    
    print('Starting LLM', '-'*25)
    results = await asyncio.gather(*tasks)
    print('LLM Finished', '-'*25)
    
    return dict(results)