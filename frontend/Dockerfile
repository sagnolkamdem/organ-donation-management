FROM node:18 as build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm cache clean --force
RUN npm install
COPY . .
EXPOSE 4200
CMD ["npm", "start"]
