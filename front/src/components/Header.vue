<template>
  <div class="app-header header-shadow">
    <div class="app-header__content">
            <div class="app-header-left">
	            <span class="info-text">Hotline</span>
              <font-awesome-icon icon="phone-alt"/>
	            <a href="tel:+420775466513">+420 775 466 513</a>
            </div>
      <div class="app-header-right">
        <HeaderUserArea :logged-in="loggedIn"/>
      </div>
    </div>
    <div class="app-header__mobile-menu">
      <div>
        <button type="button" class="hamburger close-sidebar-btn hamburger--elastic"
                v-bind:class="{ 'is-active' : isOpen }" @click="toggleMobile('closed-sidebar-open')">
          <span class="hamburger-box">
              <span class="hamburger-inner"></span>
          </span>
        </button>
      </div>
    </div>
    <div class="app-header__menu">
      <span>
        <b-button class="btn-icon btn-icon-only" variant="primary" size="sm"
                  v-bind:class="{ 'active' : isOpenMobileMenu }" @click="toggleMobile2('header-menu-open')">
          <div class="btn-icon-wrapper">
              <font-awesome-icon icon="ellipsis-v"/>
          </div>
        </b-button>
      </span>
    </div>
  </div>
</template>

<script>

  import {mapState} from 'vuex'

  import {library} from '@fortawesome/fontawesome-svg-core'
  import {faEllipsisV, faPhoneAlt} from '@fortawesome/free-solid-svg-icons'
  import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'

  import HeaderUserArea from './partials/HeaderUserArea'

  library.add(
    faEllipsisV,
	  faPhoneAlt
  );

  export default {
    name: "Header",
    components: {
      HeaderUserArea,
      'font-awesome-icon': FontAwesomeIcon,
    },
    computed: {
      ...mapState({
        loggedIn: state => state.auth.loggedIn,
        // user: state => state.auth.user,
      })
    },
    data() {
      return {
        isOpen: false,
        isOpenMobileMenu: false,
      }
    },
    methods: {
      // logout: function () {
      //   this.$store.dispatch(AUTH_LOGOUT).then(() => this.$router.push('/login'))
      // },
      toggleMobile(className) {
        const el = document.body;
        this.isOpen = !this.isOpen;

        if (this.isOpen) {
          el.classList.add(className);
        } else {
          el.classList.remove(className);
        }
      },

      toggleMobile2(className) {
        const el = document.body;
        this.isOpenMobileMenu = !this.isOpenMobileMenu;

        if (this.isOpenMobileMenu) {
          el.classList.add(className);
        } else {
          el.classList.remove(className);
        }
      },
    }
  };
</script>
