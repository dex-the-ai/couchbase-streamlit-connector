# Built verbatim from README "Getting Started" (Option 1) + "Usage" snippets.
import sys
import streamlit as st
import PIL
from couchbase_streamlit_connector.connector import CouchbaseConnector

st.title("couchbase-streamlit-connector smoke")
st.write(f"Python {sys.version.split()[0]} | streamlit {st.__version__} | pillow {PIL.__version__}")
connection = st.connection("couchbase", type=CouchbaseConnector)
st.help(connection)

connection.insert_document("222", {"key": "value"})
st.write("Inserted document with document id 222")
document = connection.get_document("222")
st.write("Retrieved document:", document)
connection.replace_document("222", {"new_key": "new_value"})
st.write("Updated document:", connection.get_document("222"))
connection.remove_document("222")
st.write("Document with id 222 deleted successfully.")

query = "SELECT * FROM `travel-sample`.`inventory`.`airline` LIMIT 5;"
result = connection.query(query)
st.write("Query result:", [row for row in result.rows()])
st.success("ALL README STEPS OK")
