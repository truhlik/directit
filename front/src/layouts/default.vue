<template>
  <div class="app-container app-theme-white">
    <transition name="fade" mode="out-in" appear>
      <Header/>
    </transition>
    <transition name="fade" mode="out-in" appear>
      <Sidebar/>
    </transition>
    <div class="app-main__outer">
      <div class="app-main__inner">
        <nuxt/>
	      <CallbackButton v-if="isClient && !hasFreePlan"></CallbackButton>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  import Header from "~/components/Header";
  import Sidebar from "~/components/Sidebar";
  import CallbackButton from "~/components/partials/CallbackButton";
  import VuePerfectScrollbar from 'vue-perfect-scrollbar';

  export default {
    name: 'app',
	  middleware: [
	    'auth',
		  'user',
		  'routing',
      'is_client',
	  ],
    components: {
      Header,
      Sidebar,
	    CallbackButton,
      VuePerfectScrollbar,
    },
	  transition: 'page',
    computed: {
      ...mapGetters({
        isClient: 'user/isClient',
        hasFreePlan: 'user/hasFreePlan',
      })
    }
  }
</script>
