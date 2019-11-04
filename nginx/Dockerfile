# Stage 2 - nginx & frontend dist
FROM nginx:1.17.4-alpine
WORKDIR /app/

COPY nginx/dev.conf /etc/nginx/nginx.conf

CMD ["nginx", "-g", "daemon off;"]
