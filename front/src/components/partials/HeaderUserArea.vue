<template>
	<div class="d-flex" v-if="loggedIn">
		<div class="header-btn-lg pr-0">
			<div class="widget-content p-0">
				<div class="widget-content-wrapper">
					<div class="widget-content-left">
						<b-dropdown toggle-class="p-0 mr-2" menu-class="dropdown-menu-lg" variant="link" no-caret right>
              <span slot="button-content">
                <div class="icon-wrapper icon-wrapper-alt rounded-circle">
                  <i class="pe-7s-user"/>
	                <span class="user-name">{{ username }}</span>
                  <font-awesome-icon class="ml-1" icon="angle-down"/>
                </div>
              </span>
							<div class="dropdown-menu-header">
								<div class="dropdown-menu-header-inner bg-info">
									<div class="menu-header-image opacity-2 dd-header-bg-6"></div>
									<div class="menu-header-content text-left">
										<div class="widget-content p-0">
											<div class="widget-content-wrapper">
												<div class="widget-content-left mr-3">
												
												</div>
<!--												<div class="widget-content-left">-->
<!--													<div class="widget-heading">{{ $auth.user.email }}</div>-->
<!--													<div class="widget-subheading opacity-8">{{ $auth.user.first_name }} {{ $auth.user.last_name }}-->
<!--													</div>-->
<!--												</div>-->
												<div class="widget-content-right m-0 d-flex align-items-stretch justify-content-around w-100">
													<nuxt-link  class="btn-pill btn-shadow btn-shine btn btn-focus mb-2"
													            :to="localePath({name:'uzivatel-upravit'})">
                                                        {{ isConsultant? $t('account.personal_credentials') : $t('account.user_credentials') }}
													</nuxt-link>
													<nuxt-link v-if="!isConsultant" class="btn-pill btn-shadow btn-shine btn btn-focus mb-2"
																			:to="localePath({name:'uzivatel-upravit', query: { active: 'password'} })">
														{{ $t('form.button.password_change') }}
													</nuxt-link>
													<b-button class="btn-pill btn-shadow btn-shine btn btn-focus mb-2"
																		@click="createOrUpdateCompany">
                                                        {{ isConsultant? $t('account.your_public_profile') : $t('account.your_profile') }}
                                                    </b-button>
												</div>
											</div>
										</div>
									</div>
								</div>
							</div>
							<ul class="nav flex-column">
								<li class="nav-item-divider nav-item"></li>
								<li class="nav-item-btn text-center nav-item">
									<button class="btn-wide btn btn-primary btn-sm"
									        @click="logout">
										{{ $t('form.button.logout') }}
									</button>
								</li>
							</ul>
						</b-dropdown>
					</div>
					<div class="widget-content-left  ml-3 header-user-info">
<!--						<div class="widget-heading">{{ user.first_name }} {{ user.last_name }}</div>-->
						<!--<div class="widget-subheading">{{ user.username }}</div>-->
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import {mapGetters, mapMutations} from 'vuex'
  import {library} from '@fortawesome/fontawesome-svg-core'
  import {faAngleDown} from '@fortawesome/free-solid-svg-icons'
  import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
  
  import { mapState } from 'vuex'

  library.add(
    faAngleDown,
  );

  export default {
    components: {
      'font-awesome-icon': FontAwesomeIcon,
    },
    props: {
      loggedIn: Boolean,
    },
      computed: {
          ...mapState({
              user: state => state.user.user
          }),
          username: function () {
              return this.user.email;
          },
          ...mapGetters({
              isClient: 'user/isClient',
              isSupplier: 'user/isSupplier',
              isConsultant: 'user/isConsultant',
          }),
	  },
    methods: {
      ...mapMutations('user', {
	      clearUser: 'clearUser'
      }),
      async logout() {
        this.clearUser();
        await this.$auth.logout();
        this.$toast.success('Logged out!');
      },
	    createOrUpdateCompany(){
            if($nuxt.$route.name == 'subjekt-id-upravit___cs') return
            this.$router.push({name:'subjekt-vytvorit___cs'});
	    }
    }
  }
</script>

<style lang="scss">
	.dropdown-toggle::after {
		/*content: unset;*/
	}
	
	.dropdown-menu {
		padding: 0;
		
		& > .dropdown-menu-header {
			margin: 0;
		}
	}
	
	.icon-wrapper {
		align-items: center;
		display: flex;
		font-size: 1.5rem;
		
		i {
			font-size: 2rem;
		}
	}
</style>
