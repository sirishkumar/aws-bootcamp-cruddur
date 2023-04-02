FROM node:16.18

ENV PORT 3000

COPY . /frontend-react-js
WORKDIR /frontend-react-js
RUN npm install --verbose --no-optional --no-audit --no-fund --no-package-lock --no-bin-links --no-shrinkwrap --only=production
EXPOSE ${PORT}
CMD ["npm", "start"]
