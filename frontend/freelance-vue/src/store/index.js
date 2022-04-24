import { createStore } from 'vuex'

export default createStore({
state: {
    user: localStorage.getItem('userId')
},
mutations: {

},
actions: {

},
getters: {
    isAuthenticated: state => !!state.user,
}
})
