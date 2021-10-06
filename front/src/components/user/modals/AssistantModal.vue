<template>
    <div>
        <b-modal  class="text-left"
                  ref="Assistant-modal"
                  hide-footer>
            <template v-slot:modal-title>
                {{ modalName }}
            </template>
            <AssistantForm @closeParent="closeModal"
                          :infoText="infoText"
                          :AssistantType="AssistantType"></AssistantForm>
        </b-modal>
    </div>
</template>

<script>
    import AssistantForm from "~/components/user/AssistantForm";
    export default {
        name: 'assistant-modal',
        props: {
            modalName: String,
            infoText: String,
            AssistantType: String,
        },
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