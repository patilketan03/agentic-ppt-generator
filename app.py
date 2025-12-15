import streamlit as st
import requests
import subprocess


st.title(":violet[Agentic PPT Generator]")
st.subheader("Generate your PPT easily using a simple prompt")


prompt = st.text_area("Describe Your Presentation",
    placeholder="Enter the topic, number of slides, key points, and any design or formatting preferences…")


if st.button(":green[Generate PPT]"):
    if prompt:
        response=requests.post(url="https://ketanspatil.app.n8n.cloud/webhook-test/55b9de36-208b-43d8-80ba-87a2f58d5319",
                               json={"prompt":prompt})
        

        if response.status_code==200:
            st.write("Success")

            output = response.json()["output"]
            output = output.replace("```python", "").replace("```", "")

            with open("generate_ppt.py", "w", encoding="utf-8") as file:
                file.write(output)


            subprocess.run(["python", "generate_ppt.py"])

with open(r"C:\Users\Admin\Desktop\Agentic-AI-Internship\PPT_Generation\power\power\Python_for_Data_Science.pptx","rb") as ppt:
        st.download_button(
            label=":green[⏬Download PPT]",
            data=ppt,
            file_name="Agentic_PPT.pptx")