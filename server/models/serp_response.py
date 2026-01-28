from typing import TypedDict, List, NotRequired

class SerpSearchMetadata(TypedDict):
    id: str
    status: str
    json_endpoint: str
    created_at: str
    processed_at: str
    google_shopping_light_url: str
    raw_html_file: str
    total_time_taken: float

class SerpSearchParameters(TypedDict):
    engine: str
    q: str
    google_domain: str
    hl: str
    gl: str
    device: str

class SerpShoppingResult(TypedDict):
    position: int
    title: str
    thumbnail: str
    source: str
    product_link: str
    product_id: str
    # NotRequired is useful for fields that might be missing entirely
    immersive_product_page_token: NotRequired[str]
    serpapi_immersive_product_api: NotRequired[str]
    serpapi_thumbnail: NotRequired[str]
    price: NotRequired[str]
    extracted_price: NotRequired[float]
    old_price: NotRequired[str]
    extracted_old_price: NotRequired[float]
    rating: NotRequired[float]
    reviews: NotRequired[int]
    source_icon: NotRequired[str]
    multiple_sources: NotRequired[bool]
    delivery: NotRequired[str]
    tag: NotRequired[str]
    extensions: NotRequired[List[str]]

class SerpResponse(TypedDict):
    search_metadata: SerpSearchMetadata
    search_parameters: SerpSearchParameters
    shopping_results: List[SerpShoppingResult]