"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
Each Pydantic model represents a collection. Class name lowercased = collection name.
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

class Lead(BaseModel):
    """
    Leads collected from the website contact form
    Collection name: "lead"
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Contact email")
    company: Optional[str] = Field(None, description="Company name")
    message: Optional[str] = Field(None, description="Project brief or message")
    services: Optional[List[str]] = Field(default_factory=list, description="Selected services of interest")
    source: Optional[str] = Field("website", description="Lead source")

# You can add more schemas (e.g., CaseStudy, Testimonial) as needed.
