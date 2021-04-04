FROM node:14.4
WORKDIR /react-app
COPY package.json package.json
RUN npm install
EXPOSE 3000
COPY . .
CMD ["npm", "run", "start"]