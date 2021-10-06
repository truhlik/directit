<template>
	<div>
		<span class="callback-button shadow-lg"
					@click="openModal">
		<i class="pe-7s-users"></i>
		</span>
		
        <!--<b-modal class="text-left"
							ref="callback-modal"
							hide-footer>
			<template v-slot:modal-title>
				{{ $t('menu.callback') }}
			</template>
			<CallbackForm @closeParent="closeModal"></CallbackForm>
        </b-modal>-->
        <b-modal
                class="text-left"
                ref="Assistant-modal"
                hide-footer>
            <template v-slot:modal-title>
                {{ $t('services.it_assistant.title') }}
            </template>
            <AssistantForm @closeParent="closeModal"
                           :infoText="$t('services.callback.info_text')"
                           ></AssistantForm><!--:AssistantType="AssistantType"-->
		</b-modal>
	</div>
</template>

<script>
    import AssistantForm from "~/components/user/AssistantForm";

	export default {
	  name: 'callback-button',
		components: {
            AssistantForm
		},
		methods: {
	    openModal() {
                this.$refs['Assistant-modal'].show();
	    },
	    closeModal: function () {
                this.$refs['Assistant-modal'].hide();
	    }
		}
	}
</script>