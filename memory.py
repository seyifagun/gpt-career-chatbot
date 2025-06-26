import chromadb

#create chromadb client
chroma_client = chromadb.Client()

# Get or create collection
try:
    # Try to get existing collection
    collection = chroma_client.get_collection(name="collection")
except:
    # Create new collection if it doesn't exist
    collection = chroma_client.create_collection(name="collection")

def seed_memory():
    try:
        # Check if documents already exist
        existing_ids = collection.get(ids=["cv1", "cv2", "visa1", "projects1"])
        if existing_ids:
            print("Memory already seeded, skipping...")
            return
    except:
        pass

    # Add new documents
    try:
        collection.add(
            documents=[
                "Tailor your resume to each job posting to increase response rate.",
                "Use active verbs like 'built', 'led', 'deployed' in your experience section.",
                "For UK visa sponsorship, look for Tier 2 licensed employers on gov.uk.",
                "Projects with Streamlit and FastAPI impress entry-level recruiters."
            ],
            metadatas=[{"topic": "cv"}, {"topic": "cv"}, {"topic": "visa"}, {"topic": "projects"}],
            ids=["cv1", "cv2", "visa1", "projects1"]
        )
        print("Memory seeded successfully")
    except Exception as e:
        print(f"Error seeding memory: {str(e)}")

def query_memory(query):
    try:
        if not query:
            return None

        result = collection.query(
            query_texts=[query],
            n_results=1
        )
        
        # Check if we got any results
        if result and result.get("documents") and result["documents"][0]:
            return result["documents"][0][0]
        return None
        
    except Exception as e:
        print(f"Error querying memory: {str(e)}")
        return None

