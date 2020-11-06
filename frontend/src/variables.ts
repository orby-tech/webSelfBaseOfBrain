import axios from 'axios'


const TEST_MODE = () => {return (window.location.host === 'localhost:8080')}
const HOST = window.location.host
const link = () => {
  if (TEST_MODE()) {
    return 'http://127.0.0.1:10000/'
  } else {
    return 'http://' + HOST
  }
}

const baseUrl = link()
const ax = (src : string , arg : any = null) => axios.post(baseUrl + src, arg);
export {
  TEST_MODE,
  baseUrl,
  ax
}
