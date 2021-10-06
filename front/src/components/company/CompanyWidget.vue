<template>
    <div class="card-shadow-primary profile-responsive card-border mb-3 card">
        <div class="dropdown-menu-header">
            <div class="dropdown-menu-header-inner bg-blue-icon">
                <button class="btn btn-primary add-stars-btn mr-1"
                        v-if="(company.testimonials).length"
                        @click="showTestimonialsModal(company)"><i class="pe-7s-star"></i></button>

                <div class="menu-header-content btn-pane-right">
                    <div class="avatar-icon-wrapper mr-2 avatar-icon-xl">
                        <div class="avatar-icon rounded">
                            <img v-if="company.image" :src="company.image" alt="Avatar 6">
                            <img v-else src="@/assets/images/empty-avatar.svg" alt="Avatar 6">
                        </div>
                    </div>
                    <div>
                        <h5 class="menu-header-title">{{ company.name }}</h5>
                        <h6 class="menu-header-subtitle">{{ company.address }}</h6>
                    </div>
                </div>

                <div class="box-tags" v-if=company.tags.length>
                    <button @click="filterByTag(company.role, tag.name)"
                            v-if="tag.name != '' || tag.name != null"
                            v-for="(tag, index) in company.tags"
                            class="mb-2 mr-2 btn btn-primary"
                            :key="tag.name">{{ tag.name }}
                    </button>
                </div>
            </div>
        </div>
        <div class="tab-content">
            <div class="tab-pane active show">
                <ul class="list-group list-group-flush">
                    <!--								<li class="list-group-item">-->
                    <!--									<div class="widget-content company-tags">-->
                    <!--										<span v-for="(tag, tagIndex) in company.tags"-->
                    <!--										     :key="tag.name"-->
                    <!--										     class="badge-cat">{{ tag.name }}-->
                    <!--										</span>-->
                    <!--										<span v-for="(category, categoryIndex) in company.categories"-->
                    <!--										     :key="category.name"-->
                    <!--										     class="badge-cat">{{ category.name }}-->
                    <!--										</span>-->
                    <!--									</div>-->
                    <!--								</li>-->
                    <li class="p-0 list-group-item">
                        <div class="grid-menu comp-boxes grid-menu-2col overflow-hidden">
                            <div class="no-gutters row">
                                <div class="col-4">
                                    <button class="btn-icon-vertical btn-square btn-transition btn btn-outline-link"
                                            @click="showOrderModal(company)">
                                        <i class="pe-7s-cart btn-icon-wrapper btn-icon-lg mb-3"> </i>
                                        <p>{{ $t('form.button.request') }}</p>
                                    </button>
                                </div>
                                <div class="col-4">
                                    <nuxt-link class="btn-icon-vertical btn-square btn-transition btn btn-outline-link"
                                               :to="localePath({name: `subjekty-type-id`, params: { id: company.id, type: companyUrls[company.role] }})">
                                        <i class="pe-7s-user btn-icon-wrapper btn-icon-lg mb-3"> </i>
                                        <p>{{ $t('form.button.profile') }}</p>
                                    </nuxt-link>
                                </div>
                                <div class="col-4">
                                    <button class="btn-icon-vertical btn-square btn-transition btn btn-outline-link"
                                            @click="showTestimonialsFormModal(company)">
                                        <i class="pe-7s-like2 btn-icon-wrapper btn-icon-lg mb-3"> </i>
                                        <p>{{ $t('testimonial.button.add') }}</p>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </div>

        <TestimonialsModal ref="childTestimonialsModal"
                           :company="company"></TestimonialsModal>
        <OrderModal ref="childOrderModal"
                    :company="company"></OrderModal>

        <TestimonialsFormModal ref="childTestimonialFormModal"></TestimonialsFormModal>
    </div>

</template>

<script>
import TestimonialsModal from "~/components/company/modals/TestimonialsModal";
import TestimonialsFormModal from "~/components/company/modals/TestimonialsFormModal";
import OrderModal from "~/components/orders/OrderModal";
import {COMPANY_URLS} from "~/helpers/constants";

export default {
    name: "CompanyWidget",
    components: {OrderModal, TestimonialsModal, TestimonialsFormModal},
    props: {
        company: Object,
    },
    data: () => ({
        companyUrls: COMPANY_URLS
    }),
    methods: {
        showTestimonialsFormModal(company) {
            this.$refs.childTestimonialFormModal.showModal(company);
        },
        showTestimonialsModal(company) {
            this.$refs.childTestimonialsModal.showModal();
        },
        showOrderModal(company) {
            this.$refs.childOrderModal.showModal();
        },
    },
}
</script>

<style scoped>

</style>