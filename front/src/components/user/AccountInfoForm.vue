<template>
	<div>
		<div class="form-con user-form-wrap">
			<h2 class="text-center">{{ isSupplier ? $t('account.account_company_administrator') : $t('account.account_administrator') }}</h2>
			<b-row>
				<b-col sm="12" class="d-flex justify-content-center">
					<b-form-group :label="$t('form.first_name')"
												label-for="id_first_name">
						<b-form-input id="id_first_name"
						              type="text"
													:placeholder="$t('form.first_name')"
													v-model="first_name">
						</b-form-input>
					</b-form-group>
				</b-col>
				<b-col sm="12" class="d-flex justify-content-center">
					<b-form-group :label="$t('form.last_name')"
												label-for="id_last_name">
						<b-form-input id="id_last_name"
						              type="text"
													:placeholder="$t('form.last_name')"
													v-model="last_name">
						</b-form-input>
					</b-form-group>
				</b-col>
				<b-col sm="12" class="d-flex justify-content-center">
			<b-form-group :label="$t('form.phone')"
										label-for="id_phone"
										description="Telefon musí být ve formátu +420777000112">
				<b-form-input id="id_phone"
				              type="text"
											:placeholder="$t('form.phone')"
											v-model="phone">
				</b-form-input>
			</b-form-group>
				</b-col>
				<b-col sm="12" class="d-flex justify-content-center">
					<b-button class="mr-2 mb-2 btn-hover-shine btn-transition"
					          variant="primary"
					          size="lg"
										@click="updateUser">
						{{ $t('form.button.save') }}
					</b-button>
					
				</b-col>
			</b-row>
		</div>
	</div>
</template>

<script>
	import { mapActions, mapMutations, mapGetters } from 'vuex'
	
	export default {
	  name: 'account-info-form',
		props: ['user'],
	  computed: {
		  phone:{
		   set(phone){
		    this.addToUser({phone});
		   },
			 get(){
		     return this.user.phone;
			 }
		  },
		  first_name:{
		   set(first_name){
		    this.addToUser({first_name});
		   },
			 get(){
		     return this.user.first_name;
			 }
		  },
		  last_name:{
		   set(last_name){
		    this.addToUser({last_name});
		   },
			 get(){
		     return this.user.last_name;
			 }
		  },
          ...mapGetters({
              isClient: 'user/isClient',
              isSupplier: 'user/isSupplier',
              isConsultant: 'user/isConsultant', 
          }),
	  },
	  methods: {
		  ...mapMutations('user', {
		    addToUser: 'addToUser'
		  }),
		  ...mapActions('user', {
		    updateUserRequest: 'updateUserRequest'
		  }),
		  updateUser(){
		    const data = {
		      userId: this.user.id,
			    userData: {
		        first_name: this.user.first_name,
		        last_name: this.user.last_name,
			      phone: this.user.phone
			    }
		    };
			 this.updateUserRequest(data);
		  }
	  }
	}
</script>