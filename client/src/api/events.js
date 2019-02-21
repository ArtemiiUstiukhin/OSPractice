import { HTTP } from './common'

export const Event = {
  add (config) {
    //return HTTP.post('/events/', config).then(response => {
     return HTTP.get('/').then(response => {
	 return response.text
    })
  }
}
