FROM arsen3d/lpbase:latest

# Set the working directory
WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV GRADIO_SERVER_PORT=8080
# Copy the requirements file
COPY . /app
RUN chmod +x app.sh
# Install the dependencies
RUN pip install uv
RUN uv pip install -r requirements.txt --system

# Copy the rest of the application code
# COPY . .
# RUN chmod +x run_app.sh