export default function ({ store }) {
  if(Object.keys(store.state.user.user).length === 0){
    return store.dispatch('user/getUser');
  }
}