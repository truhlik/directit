<template>
  <div class="custom-container bg-transparent p-0" v-if="person">
		<div class="row m-0 mt-4">
			<nuxt-link class="col-sm-12 offset-md-1 col-md-10 h-auto p-0"
			     	:key="person.id"
						:to="localePath({name: `subjekty-type-id`, params: { id: person.id, type: companyUrls[person.role] }})">
				<div class="card-shadow-primary profile-responsive card-border mb-3 card">
					<div class="dropdown-menu-header">
						<div class="dropdown-menu-header-inner bg-blue-icon">
							<div class="menu-header-image opacity-2"></div>
							<div class="menu-header-content btn-pane-right">
								<div class="avatar-icon-wrapper mr-2 avatar-icon-xl">
									<div class="avatar-icon rounded">
										<img v-if="person.image" :src="person.image" alt="Avatar 6">
										<img v-else src="@/assets/images/empty-avatar.svg" alt="Avatar 6">
									</div>
								</div>
								<div>
									<h5 class="menu-header-title">{{ person.name }}</h5>
									<h6 class="menu-header-subtitle">{{ person.address }}</h6>
								</div>
							</div>
						</div>
					</div>
				</div>
			</nuxt-link>

		</div>
  </div>
</template>

<script>
  import { COMPANY_URLS } from "~/helpers/constants";

  export default {
    name: 'person-card',
    props: {
      person: {
        type: Object,
        default: {}
      }
    },
		data: () => ({
		  companyUrls: COMPANY_URLS
		})
  }
</script>

<style>

</style>