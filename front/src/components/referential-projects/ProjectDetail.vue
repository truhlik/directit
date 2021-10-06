<template>
  <div class="custom-container card pt-5">
    <div class="mt-5">
      <div class="form-con">
        <b-row class="mb-3">
          <b-col sm="9" class="p-3">
            <b-row class="">
                <b-col sm="12" class="">
                    <h1 class="project-title">{{ project.title }}</h1>
                </b-col>
                <!-- <b-col sm="6" class="">
                    <p class="contact-name">{{ project.contact_name }}</p>
                </b-col>
                <b-col sm="6" class="">
                    <p class="contact-email">{{ project.contact_email }}</p>
                </b-col> -->
            </b-row>
          </b-col>
          <b-col sm="3" class="p-3">
            <nuxt-link
              class="text-black-50"
              v-if="canEdit"
              :to="
                localePath({
                  name: 'referencni-projekty-id-upravit',
                  params: { id: project.id },
                })
              "
            >
              <b-button
                class="btn-transition btn-hover-shine custom-lg"
                variant="primary"
                size="lg"
              >
                {{ $t("form.button.update") }}
              </b-button>
            </nuxt-link>
          </b-col>
          <b-col sm="12" class="p-3" v-if="project.sector">
            <span class="title-tags d-block mb-2">
              {{ $t("form.sector") }}
            </span>
            <span class="mb-2 mr-2 btn btn-info">
              {{ project.sector_obj.name }}
            </span>
          </b-col>
          <b-col sm="12" v-if="project.category">
            <!--                        <pre>{{project}}</pre>-->
            <CategoriesComponent
              accessoriesType="categories"
              :title="$t('form.categories')"
              :propCategories="
                project && project.category_obj ? [project.category_obj] : null
              "
              :modelWithCategories="project"
              helpText=""
              :required="false"
              :singleOnly="true"
              :senToApi="false"
              :disabled="true"
            />
          </b-col>
          <b-col sm="12" v-if="project.products.length">
            <ProductsComponent
              accessoriesType="products"
              :title="$t('form.products')"
              :modelWithProducts="project"
              helpText=""
              :required="false"
              :propProducts="project.products_obj"
              :disabled="true"
            />
          </b-col>
          <b-col
            sm="12"
            class="p-3"
            v-if="project.problem_text"
          >
            <b-row>
              <b-col sm="12" class="title-texts">
                <font-awesome-icon class="mx-1" icon="puzzle-piece" />
                {{$t('form.problem_text')}}
              </b-col>
              <b-col sm="12">
                {{ project.problem_text }}
              </b-col>
            </b-row>
          </b-col>
          <b-col
            sm="12"
            class="p-3"
            v-if="project.solution_text"
          >
            <b-row>
              <b-col sm="12" class="title-texts">
                <font-awesome-icon class="mx-1" icon="project-diagram" />
                {{$t('form.solution_text')}}
              </b-col>
              <b-col sm="12">
                {{ project.solution_text }}
              </b-col>
            </b-row>
          </b-col>
          <b-col
            sm="12"
            class="p-3"
            v-if="project.benefits_text"
          >
            <b-row>
              <b-col sm="12" class="title-texts">
                <font-awesome-icon class="mx-1" icon="money-bill" />
                {{$t('form.benefits_text')}}
              </b-col>
              <b-col sm="12">
                {{ project.benefits_text }}
              </b-col>
            </b-row>
          </b-col>
          <b-col sm="12" class="p-3">
              <FileComponent :can-be-updated="false"
                  :files="project.files_obj"
              />
          </b-col>
        </b-row>
        <b-row class="mb-3 solver" v-if="project.solver_obj && isClient">
          <b-col sm="12">
            <company-widget :company="project.solver_obj"></company-widget>
          </b-col>
        </b-row>
      </div>
    </div>
  </div>
</template>

<script>
import CompanyWidget from "../company/CompanyWidget";
import CategoriesComponent from "~/components/features/CategoriesComponent";
import ProductsComponent from "~/components/features/ProductsComponent";
import {mapGetters, mapState} from "vuex";
import { SECTOR_OPTIONS } from "./ProjectForm";
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faPuzzlePiece,
  faProjectDiagram,
  faMoneyBill,
  faLayerGroup,
} from "@fortawesome/free-solid-svg-icons";
import FileComponent from "../features/FileComponent";

library.add(faPuzzlePiece, faProjectDiagram, faMoneyBill, faLayerGroup);

export default {
  name: "ProjectDetail",
  components: {
      FileComponent,
    CompanyWidget,
    CategoriesComponent,
    ProductsComponent,
  },
  data: () => ({
    sectorOptions: SECTOR_OPTIONS,
  }),
  computed: {
    ...mapState({
      project: (state) => state.projects.refProject,
      user: (state) => state.user.user,
    }),
    ...mapGetters({
      isClient: 'user/isClient',
      isSupplier: 'user/isSupplier',
      isConsultant: 'user/isConsultant',
    }),
    sector() {
      return this.sectorOptions.find((x) => x.value == this.project?.id)?.text;
    },
    canEdit() {
      return this.project?.can_edit;
    },
  },
};
</script>

<style scoped lang='scss'>
.project-title {
  font-size: 25px;
  //padding: 15px 0;
  font-weight: 400; 
  color: #495057;
}
.contact-name {
  font-size: 15px;
  //padding: 15px 0;
  font-weight: 600;
}
.contact-email {
  font-size: 15px;
  //padding: 15px 0;
}
.solver {
    margin: auto;
    max-width: 500px;
}
.title-texts {
    color: #1e6294;
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
    text-transform: capitalize;
}
</style>