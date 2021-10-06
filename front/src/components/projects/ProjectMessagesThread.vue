<template>
    <div class="messagesThread"> <!--v-if="messages && messages.length"-->
        <div v-if="messages">
            <!--{{messages.results}}-->
            <!--{{messages.pagination}}-->
            <ProjectMessage :parent="parent" :thread="thread" :message="message" v-for="(message, index) in messages.results"
                            :key="message.id"></ProjectMessage>
            <div v-if="parent!=='root' && messages.pagination.next && !loadingMore" class="py-2">
                <b-button block variant="outline-secondary" @click="loadMore">{{$t('company.loadMore')}}</b-button>
            </div>
            <div v-if="loadingMore">
                <b-spinner variant="primary" label="Spinning"></b-spinner>
            </div>
        </div>
    </div>
</template>

<script>
    import ProjectMessageForm from "./ProjectMessageForm";
    import ProjectMessagesThread from "./ProjectMessagesThread";
    import {mapState} from 'vuex'
    import ProjectMessage from "./ProjectMessage";

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
        name: "project-messages-thread",
        props: {
            parent: String | Number,
            thread: String | Number,
        },
        components: {ProjectMessage, ProjectMessagesThread, ProjectMessageForm},
        computed: {
            ...mapState({
                messages: function (state) {
                    return state.projects.projectsMessages[this.thread] ? state.projects.projectsMessages[this.thread][this.parent] : null
                },
                loadingMore: function (state) {
                    return state.projects.projectsMessagesLoading[this.thread] ? state.projects.projectsMessagesLoading[this.thread][this.parent] == true : false
                }
            }),
        },
        data: () => ({
            //pagesLoaded: 1,
            //pageSize: 5,
        }),
        created() {
            //console.log('thread created', this.messages)
            if (!this.messages) {
                this.$store.dispatch('projects/getProjectMessages', {
                    id: this.thread,
                    parent: this.parent/* === 'root' ? null : this.parent*/,
                    //page: this.pagesLoaded,
                    //size: this.pageSize,
                })
            }
        },
        methods: {
            loadMore() {
                //console.log('loadMore', this.parent, this.messages?.pagination.next);
                if (!this.messages?.pagination.next) return;
                //this.pagesLoaded++;
                this.$store.dispatch('projects/getProjectMessages', {
                    id: this.thread,
                    parent: this.parent/* === 'root' ? null : this.parent*/,
                    //page: this.pagesLoaded,
                    //size: this.pageSize,
                })
            },
            onScroll(/*{target: {scrollTop, clientHeight, scrollHeight}}*/) {
                /*console.log('onScroll', window.innerHeight, window.scrollY, document.body.offsetHeight, window.innerHeight + window.scrollY);
                if ((window.innerHeight + window.scrollY + 1) >= document.body.offsetHeight) {
                    //console.log('bottom');
                    this.loadMore();
                }*/
                let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight >= document.documentElement.offsetHeight -2
                //console.log(bottomOfWindow, document.documentElement.scrollTop + window.innerHeight, document.documentElement.offsetHeight)
                if(bottomOfWindow) this.loadMore()
            },
        },
        mounted() {
            if (this.parent == 'root') window.addEventListener("scroll", this.onScroll)
        },
        beforeDestroy() {
            if (this.parent == 'root') window.removeEventListener("scroll", this.onScroll)
        },
    }
</script>

<style scoped>

</style>