FROM nginx

WORKDIR /nginx

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN rm /etc/nginx/conf.d/*
COPY nginx.conf /etc/nginx/conf.d/nginx.conf

EXPOSE 80

CMD bash -c "nginx -g 'daemon off;'"
