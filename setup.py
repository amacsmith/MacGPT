from setuptools import setup, find_packages

setup(
    name="ai_interface",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.68.1",
        "uvicorn==0.15.0",
        "pydantic==1.8.2",
        "python-dotenv==0.19.1",
        "transformers==4.11.3",
        "torch==1.9.1",
        "faiss-cpu==1.7.1",
        "sqlalchemy==1.4.25",
        "requests==2.26.0",
        "prometheus-client==0.11.0",
        "redis==3.5.3",
    ],
)