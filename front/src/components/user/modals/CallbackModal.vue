<template>
	<div>
		<b-modal  class="text-left"
							ref="callback-modal"
							hide-footer>
			<template v-slot:modal-title>
				{{ modalName }}
			</template>
			<CallbackForm @closeParent="closeModal"
										:infoText="infoText"
										:callbackType="callbackType"></CallbackForm>
		</b-modal>
	</div>
</template>

<script>
	import CallbackForm from "~/components/user/CallbackForm";
	export default {
	  name: 'callback-modal',
		props: {
	    modalName: String,
			infoText: String,
			callbackType: String
		},
		components: {
	    CallbackForm
		},
		methods: {
	    openModal() {
	      this.$refs['callback-modal'].show();
	    },
	    closeModal: function () {
	      this.$refs['callback-modal'].hide();
	    }
		}
	}
</script>