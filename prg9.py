!pip install wikipedia pydantic 
import wikipedia 
import re 
from pydantic import BaseModel 
class InstitutionInfo(BaseModel): 
founder: str 
founded_year: str 
branches: str 
employees: str 
summary: str 
institution = input("Enter Institution Name: ") 
try: 
# Disable auto suggestion to avoid wrong page names 
summary = wikipedia.summary(institution, sentences=4, auto_suggest=False) 
page = wikipedia.page(institution, auto_suggest=False).content 
# Extract founder 
founder_match = re.search(r"founded by ([A-Za-z\s]+)", page, re.IGNORECASE) 
founder = founder_match.group(1) if founder_match else "Not available" 
# Extract year 
year_match = re.search(r"\b(18|19|20)\d{2}\b", page) 
founded_year = year_match.group(0) if year_match else "Not available" 
branches = "Multiple campuses / departments" 
27 
employees = "Information available on Wikipedia" 
result = InstitutionInfo( 
founder=founder, 
founded_year=founded_year, 
branches=branches, 
employees=employees, 
summary=summary 
) 
print("\nInstitution Details\n") 
print("Founder:", result.founder) 
print("Founded Year:", result.founded_year) 
print("Branches:", result.branches) 
print("Employees:", result.employees) 
print("Summary:", result.summary) 
except wikipedia.exceptions.PageError: 
print("The page was not found. Please enter a valid institution name.") 
except wikipedia.exceptions.DisambiguationError as e: 
print("Multiple results found. Try one of these:") 
print(e.options[:5]) 
