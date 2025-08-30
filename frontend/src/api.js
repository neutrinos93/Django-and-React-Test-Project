// We will write an interceptor to write all the headers
// using axios. If we have an access code it will add it

import axios from "axios"
import { ACCESS_TOKEN } from "./constants"

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
})

// Look in localstorage, if we have access token we will add it to header
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN)
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    (error) => {
        return Promise.reject(error)
    }
)

// We will use this objects to send requests
// axios will intercept the requests
export default api