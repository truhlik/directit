<template>
    <div class="p-2 d-flex justify-content-end flex-wrap">
        <b-form-textarea
                id="textarea"
                v-model="text"
                :placeholder="$t('form.message_placeholder')"
                rows="3"
                max-rows="6"
        ></b-form-textarea>
        <b-button variant="success" class="mr-1 mt-1"
                  @click="submit()" :disabled="submitting || !text || !text.length">
            <font-awesome-icon class="ml-1"
                               icon="reply"
                               v-if="!submitting"
            />
            <b-spinner class="ml-1" small
                       v-if="submitting"
                       variant="white"
            ></b-spinner>
            &nbsp;
            {{$t('form.button.submit')}}
        </b-button>
    </div>
</template>

<script>
    import {mapActions} from 'vuex'
    import {library} from '@fortawesome/fontawesome-svg-core'
    import {
        faTimes,
        faReply,
    } from '@fortawesome/free-solid-svg-icons'
    import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'

    library.add(
        faTimes,
        faReply
    );
    export default {
        name: "ProjectMessageForm",
        data: () => ({
            text: null,
            submitting: false,
        }),
        props: {
            parent: String | Number,
            thread: String | Number,
        },
        methods: {
            ...mapActions('projects', {
                submitMessage: 'submitMessage',
            }),
            async submit() {
                this.submitting = true;
                //console.log('submit()', this.parent, this.text, this.thread)
                try {
                    const result = await this.submitMessage({parent: this.parent, text: this.text, threadId: this.thread})
                    this.$emit('submit', result);
                    this.text = '';
                } catch (e) {
                    console.error($nuxt.$t('callback.error'));
                }
                this.submitting = false;
            },

        }
    }
</script>

<style scoped>

</style>