# Use the official nginx image as a base
FROM nginx:alpine

# Remove the default nginx static assets
RUN rm -rf /usr/share/nginx/html/*

# Temporary for debugging
# Install openssh for SSH capabilities
RUN apk add --no-cache openssh

# Temporary for debugging, curl
RUN set -ex; \
    apt-get -y install --no-install-recommends \
        ca-certificates \
        curl=7.64.0-4+deb10u1 \
        unzip=6.0-23+deb10u1 \
        coreutils=8.30-3 \
        lsb-release build-essential ssh-client apt-transport-https \
        python gnupg



# Copy our static site to nginx's public folder
COPY index.html /usr/share/nginx/html/index.html

# Set correct permissions for index.html
RUN chmod 644 /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
