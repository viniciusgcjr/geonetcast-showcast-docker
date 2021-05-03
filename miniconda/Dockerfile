
FROM continuumio/miniconda3

WORKDIR /app

#RUN echo "python /app/showcast/Scripts/showcast_start.py" > /app/entrypoint.sh && \
#    chmod +x /app/entrypoint.sh


# Create the environment:
COPY environment.yaml .
RUN conda env create -f environment.yaml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "showcast", "/bin/bash", "-c"]

# The code to run when container is started:
#COPY run.py .
#ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "showcast", "python", " /app/showcast/Scripts/showcast_start.py"]
