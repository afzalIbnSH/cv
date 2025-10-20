from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

# Set up the new CV content
cv_text = """
AFZAL SHAHUL HAMEED
Senior Software Engineer
Email: aflibnush@gmail.com | Phone: +91 99952 80001
LinkedIn: linkedin.com/in/afzalshahulhameed

SUMMARY
Senior Backend Engineer with 9 years of experience designing and building scalable systems
across fast-moving startups and product-driven teams. Proficient in Python and Node.js,
with working knowledge of Go and a strong foundation in cloud-native architectures on AWS.

I have successfully contributed to a wide range of domains, from AI-powered platforms and
data infrastructure to internal tools and customer-facing applications. I've built services
from scratch, resolved critical issues and optimized performance. Actively focused on creating
product impact through robust architecture and thoughtful engineering.

SKILLS
- Languages: Python, Node.js, TypeScript, Go (basic)
- Frameworks: FastAPI, NestJS, Express, Django
- Tools & Tech: AWS (Lambda, S3, API Gateway, DynamoDB, SQS), PostgreSQL, MongoDB, Redis,
  Clickhouse, Milvus, Retool, RevenueCat, Qdrant, Rudderstack, Google BigQuery.
- Practices: System Design, Microservices, Event-Driven Architectures, API Design,
  Vector Search, LLMs.

WORK EXPERIENCE

Senior Software Engineer — Locus.sh, Bangalore, India
Jan 2025 – Present
- Built the initial RAG-powered backend of an Agentic-AI experiment with Python, FastAPI, LLMs, MongoDB and Qdrant.

Senior Software Engineer — Blend, Bangalore, India
Feb 2022 – Jun 2024
- Helped scale Blend’s AI-native design software from 0 to 14,000 pro subscribers.
- Integrated RevenueCat for subscription monetization in core Next.js backend.
- Created a credit-based monetization microservice in Go, later extended for enterprise API billing.
- Built a multi-tenant analytics system using NestJS, Rudderstack, and Clickhouse.
- Exposed design features via enterprise APIs using NestJS.
- Switched recipe search to vector-based using Milvus.
- Integrated LLM + Diffusion model (Imagen2) for one-shot logo generation.
- Built “Auto Designs” using Gemini Pro 1.5 to auto-generate designs based on user behavior.
- Developed personalized user notification workflows based on behavioral data.

Senior Software Engineer — Freightwalla, Mumbai, India
Nov 2020 – Jan 2022
- Built customer notification preference management into Express-based core service.
- Automated shipping line interactions (document download and booking).
- Improved core search functionality.
- Developed a Python-based microservice for streamlining operations.

Senior Software Engineer — Tarams, Bangalore, India
Dec 2018 – Oct 2020
- Worked on event-driven AWS Lambda services for flight delay prediction.
- Developed product sync workflows for a Home Depot-linked e-commerce platform.

Software Engineer — Tarams, Bangalore, India
Jun 2015 – Apr 2018
- Enhanced Django-based monolithic web apps.
- Improved Express APIs and CLI tools for Datacoral’s data infrastructure product.
- Enhanced “collect slices” AWS Lambdas for syncing external data into data warehouses.

EDUCATION
Bachelor of Computer Applications (BCA)
MES College Marampally (MG University), Kerala, India
2009 – 2012
"""

# Create PDF
buffer = BytesIO()
pdf_canvas = canvas.Canvas(buffer, pagesize=A4)
width, height = A4

# Simple text rendering (for more complex formatting, use platypus or a template engine)
text_object = pdf_canvas.beginText(40, height - 50)
text_object.setFont("Helvetica", 10)
for line in cv_text.strip().split("\n"):
    text_object.textLine(line.strip())
pdf_canvas.drawText(text_object)
pdf_canvas.showPage()
pdf_canvas.save()

# Save PDF to file
output_path = "Afzal_Shahul_Hameed_CV_Nov2025.pdf"
with open(output_path, "wb") as f:
    f.write(buffer.getvalue())
