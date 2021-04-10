FROM ubuntu

RUN apt-get update && apt-get install -y curl unzip

# https://geonetcast.wordpress.com/2021/03/23/new-showcast-release-v-2-3-0/
ARG SHOWCAST_URL
ENV SHOWCAST_URL ${SHOWCAST_URL:-https://www.dropbox.com/s/t5q450g3iznjqzy/SHOWCast_v_2_3_0.zip?raw=1}

WORKDIR /app

RUN curl -L ${SHOWCAST_URL} -o showcast.zip && \
    unzip showcast.zip -d /app && \
    mv SHOWCast_v_2_3_0 /app/showcast && \ 
    rm -rf showcast.zip

RUN echo "python /app/showcast/Scripts/showcast_start.py" > /app/entrypoint.sh && \
    chmod +x /app/entrypoint.sh

WORKDIR /app/showcast

CMD /app/entrypoint.sh
