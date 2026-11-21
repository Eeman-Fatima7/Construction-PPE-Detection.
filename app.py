
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import pandas as pd
from pathlib import Path

# 1. Configure the application
st.set_page_config(
    page_title="Smart PPE Detection",
    page_icon="🦺",
    layout="wide"
)

# 2. Application title
st.title("🦺 Smart Construction PPE Detection")

st.write(
    "Upload a construction-site image to detect "
    "helmets, safety vests, workers and PPE violations."
)

st.divider()

# 3. Load your trained YOLO model
@st.cache_resource
def load_model():

    model_path = Path(__file__).parent / "best.pt"

    if not model_path.exists():
        raise FileNotFoundError(
            "best.pt is missing from the project folder."
        )

    return YOLO(str(model_path))


try:
    model = load_model()

    st.success("YOLO model loaded successfully!")

except Exception as e:
    st.error(f"Model loading error: {e}")
    st.stop()

# 4. Upload image
uploaded_file = st.file_uploader(
    "Upload a construction-site image",
    type=["jpg", "jpeg", "png"]
)

# 5. Confidence threshold slider
confidence = st.slider(
    "Adjust Detection Confidence",
    min_value=0.10,
    max_value=0.90,
    value=0.25,
    step=0.05
)

# 6. Perform object detection
if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    image_array = np.array(image)

    results = model.predict(
        source=image_array,
        conf=confidence,
        imgsz=640,
        verbose=False
    )

    result = results[0]

    # Generate image with bounding boxes
    annotated_image = result.plot()[:, :, ::-1]

    # 7. Display original and detected images
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Detected Objects")
        st.image(
            annotated_image,
            use_container_width=True
        )

    st.divider()

    # 8. Extract object information
    detections = []

    for box in result.boxes:

        class_id = int(box.cls[0])

        class_name = result.names[class_id]

        score = float(box.conf[0])

        detections.append({
            "Object": class_name,
            "Confidence (%)": round(score * 100, 2)
        })

    # 9. Display detection summary
    st.subheader("📊 Detection Summary")

    if len(detections) > 0:

        df = pd.DataFrame(detections)

        col1, col2 = st.columns(2)

        col1.metric(
            "Total Objects",
            len(detections)
        )

        col2.metric(
            "Different Classes",
            df["Object"].nunique()
        )

        st.subheader("Detection Details")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        # 10. Detect potential PPE violations
        violations = df[
            df["Object"].isin(["no-helmet", "no-vest"])
        ]

        if not violations.empty:

            st.error(
                f"⚠️ {len(violations)} potential PPE "
                "violations detected!"
            )

        else:

            st.success(
                "No missing PPE detections found."
            )

    else:

        st.warning(
            "No objects detected. Try another image "
            "or lower the confidence threshold."
        )

else:

    st.info(
        "Please upload an image to start detection."
    )
