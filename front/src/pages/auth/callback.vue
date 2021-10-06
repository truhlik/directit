<template>
  <b-container>
    <Logo/>
    <h1 class="title">
      redirecting back to admin...
    </h1>
  </b-container>
</template>

<script>
import Logo from '~/components/Logo.vue'

export default {
  auth: false,
  components: {
    Logo
  },
  asyncData(context) {
    if (context.query.code) {
      context.$auth.getToken('social');
    } else {
      context.app.router.push(context.app.localePath({name:'auth-login'}));
    }
  },
}
</script>

<style>
  .container {
    margin: 0 auto;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  .title {
    font-weight: 300;
    font-size: 42px;
    color: #526488;
    word-spacing: 5px;
    padding-bottom: 15px;
  }
</style>
