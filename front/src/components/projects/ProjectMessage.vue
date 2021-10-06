<template>
    <div class="card border-primary mb-4 message">
        <div class="card-header text-white bg-primary">
            <div class="media flex-wrap w-100 align-items-center">
                <!--<img alt="" class="d-block ui-w-40 rounded-circle" style="width: 40px; height: auto;">-->
                <div class="media-body ml-3">
                    <span v-if="message.owner">
                        {{message.owner.first_name}}
                        {{message.owner.last_name}}
                    </span>
                    <div class="text-muted small">
                        <TimeAgo :previous-date="message.updated_at" class="text-white"></TimeAgo>
                    </div>
                </div>
                <!--<div class="text-muted small ml-3">
                    <div>Member since <strong>01/12/2017</strong></div>
                    <div><strong>1,234</strong> posts</div>
                </div>-->
            </div>
        </div>
        <div class="card-body">
            <div class="media">
                <div class="media-body ml-4">
                    <div class="mt-2">
                        {{message.text}}
                    </div>
                    <div class="small mt-2">
                    </div>
                </div>
            </div>
        </div>
        <div class="card-footer d-flex flex-wrap justify-content-between align-items-center px-0 pt-0 pb-3">
            <div class="px-4 pt-3">
                <!--<span class="text-muted d-inline-flex align-items-center align-middle">
                    <i class="lnr-heart text-danger fsize-3"></i>&nbsp;
                    <span class="align-middle">48</span>
                </span>
                <span class="text-muted d-inline-flex align-items-center align-middle ml-4">
                    <i class="lnr-eye text-muted fsize-3"></i>&nbsp;
                    <span class="align-middle">1,203</span>
                </span>-->
                <button type="button" class="btn btn-secondary" v-if="!repliesExpanded && (message.replies || repliesCount)"
                        @click="repliesExpanded=true">
                    <font-awesome-icon class="ml-1"
                                       icon="comments"
                    />&nbsp; {{$t('form.button.show_replies')}} ({{repliesCount ? repliesCount : message.replies}})
                </button>
                <button type="button" class="btn btn-warning" v-if="repliesExpanded && (message.replies || repliesCount)"
                        @click="repliesExpanded=false">
                    <font-awesome-icon class="ml-1"
                                       icon="minus-circle"
                    />&nbsp; {{$t('form.button.hide_replies')}}
                </button>
            </div>
            <div class="px-4 pt-3">
                <button type="button" class="btn btn-primary" v-if="!reply"
                        @click="reply=true">
                    <font-awesome-icon class="ml-1"
                                       icon="comment"
                    />&nbsp; {{$t('form.button.reply')}}
                </button>
                <button type="button" class="btn btn-danger" v-if="reply"
                        @click="reply=false">
                    <font-awesome-icon class="ml-1"
                                       icon="times"
                    />&nbsp; {{$t('form.button.close')}}
                </button>
            </div>
            <div class="w-100">
                <ProjectMessageForm v-if="reply" @submit="replySubmitted($event)" :parent="message.id" :thread="thread"></ProjectMessageForm>
            </div>
        </div>
        <div class="pl-4 pr-2" v-if="repliesExpanded">
            <ProjectMessagesThread :parent="message.id" :thread="thread"></ProjectMessagesThread>
        </div>
    </div>
</template>

<script>
    import {mapState} from 'vuex'
    import ProjectMessageForm from "./ProjectMessageForm";
    import ProjectMessagesThread from "./ProjectMessagesThread";
    import {library} from '@fortawesome/fontawesome-svg-core'
    import {
        faTimes,
        faReply,
        faComment,
        faComments,
        faMinusCircle,
    } from '@fortawesome/free-solid-svg-icons'
    import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
    import TimeAgo from "../global/TimeAgo";

    library.add(
        faTimes,
        faReply,
        faComment,
        faComments,
        faMinusCircle,
    );

    export default {
        name: "ProjectMessage",
        components: {
            TimeAgo,
            ProjectMessagesThread,
            ProjectMessageForm
        },
        props: {
            parent: String | Number,
            thread: String | Number,
            message: Object,
        },
        data: () => ({
            reply: false,
            repliesExpanded: false,
            //repliesSubmitted: []
        }),
        beforeCreate: function () {
            this.$options.components.ProjectMessagesThread = require('./ProjectMessagesThread.vue').default     //nescessary due to circullar component import (edge case in Vue)
        },
        methods: {
            replySubmitted(reply) {
                //console.log('replySubmitted', reply)
                this.reply = false;
                this.repliesExpanded = true;
                //this.repliesSubmitted.push(reply)
            }
        },
        computed: {
            ...mapState({
                repliesCount: function (state) {
                    return state.projects.projectsMessages[this.thread] && state.projects.projectsMessages[this.thread][this.message.id] ?
                        state.projects.projectsMessages[this.thread][this.message.id].results?.length : null
                },
            }),
        }
    }
</script>

<style scoped>
    .message {
        border-width: 1px;
    }
</style>