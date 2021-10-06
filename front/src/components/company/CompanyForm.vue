<template>
  <div
    id="company-form-wrap"
    class="custom-container card pt-5"
  >
    <b-card
      v-if="!isClient"
      :title="isSupplier ? $t('account.completation_tips_title_supplier') : $t('account.completation_tips_title_consultant')"
      style="box-shadow: none"
      class="mb-2 d-flex flex-wrap justify-content-center text-center"
    >
      <b-card-text class="d-flex flex-wrap justify-content-center align-items-stretch">
        <b-nav
          pills
          fill
          justified
        >
          <b-nav-item
            v-if="isSupplier"
            href="#company-logo"
          >
            <font-awesome-icon icon="lightbulb" />
            {{$t('account.completation_tips.tip2')}}
          </b-nav-item>
          <b-nav-item
            v-if="isSupplier"
            href="#company-form"
          >
            <font-awesome-icon icon="lightbulb" />
            {{$t('account.completation_tips.tip3')}}
          </b-nav-item>
          <b-nav-item href="#component-form-tags">
            <font-awesome-icon icon="lightbulb" />
            {{$t('account.completation_tips.tip4')}}
          </b-nav-item>
          <b-nav-item href="#component-form-categories">
            <font-awesome-icon icon="lightbulb" />
            {{$t('account.completation_tips.tip5')}}
          </b-nav-item>
          <b-nav-item
            v-if="isSupplier"
            href="#component-form-categories"
          >
            <font-awesome-icon icon="lightbulb" />
            {{$t('account.completation_tips.tip6')}}
          </b-nav-item>
          <b-nav-item
            :to="{ name: 'subjekt-referencni-projekt___cs' }"
            v-if="isConsultant"
          >
            <font-awesome-icon icon="lightbulb" />
            {{$t('account.completation_tips.tip8')}}
          </b-nav-item>
        </b-nav>
      </b-card-text>
    </b-card>

    <div
      v-if="(isSupplier || isConsultant) && (!(company.role === 'CLIENT') && updateCompany)"
      class="form-con company-form-con mb-3"
    >
      <b-row>
        <b-col
          sm="12"
          class=""
        >
          <label
            v-if="!company.image"
            :key="company.image"
            class="company-logo shadow"
            for="company-logo"
          >
            {{isSupplier ? $t('form.logo_company') : $t('form.profile_image')}}
          </label>
          <label
            v-else
            class="img-label"
            for="company-logo"
          >
            <b-img
              :src="company.image"
              class="logo-img shadow"
            >

            </b-img>
          </label>
          <input
            id="company-logo"
            type="file"
            name="image"
            ref="image"
            accept="image/*"
            @change="setImage"
          />
        </b-col>
      </b-row>
    </div>

    <div
      class="form-con company-form-con"
      id="company-form"
    >
      <form @submit.prevent="handleCompanyForm">
        <b-row class="mb-4">
          <b-col sm="12">
            <label>{{ $t('form.ico') }}</label>
          </b-col>
          <b-col sm="6">
            <b-form-group>
              <b-form-input
                v-model="reg_number"
                :class="{ 'error' : objectError.reg_number }"
                @input="debounceRegNumberInput();validate('reg_number')"
              >
              </b-form-input>
              <span
                class="text-danger"
                v-for="(error, index) in objectError.reg_number"
                :key="index"
              >{{ error }}<br></span>
            </b-form-group>
          </b-col>
          <b-col
            sm="6"
            v-if="!company.id"
          >
            <b-button
              class="mr-2 mb-2 w-100 btn-hover-shine btn-transition"
              variant="primary"
              @click="LoadCompanyByIco(reg_number)"
            >
              {{ $t('company.buttons.fill_company_detail') }}
            </b-button>
          </b-col>
        </b-row>
        <b-row class="mb-4">
          <!--<b-col sm="12">
				<b-form-radio-group class="roles-btns"
				                    buttons
				                    button-variant="primary"
				                    v-if="!updateCompany"
				                    v-model="role"
				                    :options="radioFilterOptions"
				                    @change="changeRadioFilter"/>
				
				<b-form-radio-group class="roles-btns"
				                    buttons
				                    button-variant="primary"
				                    v-if="updateCompany"
				                    v-model="role"
				                    :options="radioUpdateOptions"/>
			</b-col>-->
        </b-row>
        <b-row class="">
          <b-col sm="6">
            <b-form-group
              id="name-group"
              :label="isSupplier ? $t('form.name') : $t('form.first_name')"
              label-for="company_name"
              label-class="required"
            >
              <b-form-input
                id="company_name"
                :class="{ 'error' : objectError.name }"
                type="text"
                v-model="name"
                v-bind:placeholder="$t('form.name')"
                :required="true"
                @input="validate('name')"
              >
              </b-form-input>
              <span
                class="text-danger"
                v-for="(error, index) in objectError.name"
                :key="index"
              >{{ error }}<br></span>
            </b-form-group>
          </b-col>
          <b-col sm="6">
            <b-form-group
              id="email-group"
              label-for="company_email"
              :label="$t('form.email')"
            >
              <b-form-input
                id="company_email"
                type="email"
                v-model="email"
                v-bind:placeholder="$t('form.email')"
              >
              </b-form-input>
              <span
                class="text-danger"
                v-for="(error, index) in objectError.email"
                :key="index"
              >{{ error }}<br></span>
            </b-form-group>
          </b-col>
          <b-col sm="6">
            <b-form-group
              id="phone-group"
              label-for="company_phone"
              :label="$t('form.phone')"
            >
              <b-form-input
                id="company_phone"
                type="text"
                v-model="phone"
                v-bind:placeholder="$t('form.phone')"
              >
              </b-form-input>
              <span
                class="text-danger"
                v-for="(error, index) in objectError.phone"
                :key="index"
              >{{ error }}<br></span>
            </b-form-group>
          </b-col>
          <b-col sm="6" v-if="isSupplier">
            <b-form-group
              id="web-group"
              label-for="company_web"
              :label="$t('form.website')"
            >

              <b-form-input
                id="company_web"
                type="text"
                v-model="web"
                v-bind:placeholder="$t('form.website')"
              >
              </b-form-input>
              <span
                class="text-danger"
                v-for="(error, index) in objectError.web"
                :key="index"
              >{{ error }}<br></span>
            </b-form-group>
          </b-col>
          <b-col sm="6">
            <b-form-group
              id="city-group"
              label-for="company_city"
              :label="$t('form.city')"
            >

              <b-form-input
                id="company_city"
                type="text"
                v-model="city"
                v-bind:placeholder="$t('form.city')"
              >
              </b-form-input>
              <span
                class="text-danger"
                v-for="(error, index) in objectError.city"
                :key="index"
              >{{ error }}<br></span>
            </b-form-group>
          </b-col>
          <b-col sm="6">
            <b-form-group
              id="street-group"
              label-for="company_street"
              :label="$t('form.street')"
            >
              <b-form-input
                id="company_street"
                type="text"
                v-model="street"
                v-bind:placeholder="$t('form.street')"
              >
              </b-form-input>
              <span
                class="text-danger"
                v-for="(error, index) in objectError.street"
                :key="index"
              >{{ error }}<br></span>
            </b-form-group>
          </b-col>
          <b-col sm="6">
            <b-form-group
              id="street_number-group"
              label-for="company_street_number"
              :label="$t('form.street_number')"
            >
              <b-form-input
                id="company_street_number"
                type="text"
                v-model="street_number"
                v-bind:placeholder="$t('form.street_number')"
              >
              </b-form-input>
              <span
                class="text-danger"
                v-for="(error, index) in objectError.street_number"
                :key="index"
              >{{ error }}<br></span>
            </b-form-group>
          </b-col>
          <b-col sm="6">
            <b-form-group
              id="zip-group"
              label-for="company_zip"
              :label="$t('form.zip')"
            >
              <b-form-input
                id="company_zip"
                type="text"
                v-model="zip"
                v-bind:placeholder="$t('form.zip')"
              >
              </b-form-input>
              <span
                class="text-danger"
                v-for="(error, index) in objectError.zip"
                :key="index"
              >{{ error }}<br></span>
            </b-form-group>
          </b-col>
          <b-col sm="6">
            <b-form-group
              id="dic-group"
              label-for="company_dic"
              :label="$t('form.dic')"
            >
              <b-form-input
                id="company_dic"
                type="text"
                v-model="dic"
                v-bind:placeholder="$t('form.dic')"
              >
              </b-form-input>
              <span
                class="text-danger"
                v-for="(error, index) in objectError.dic"
                :key="index"
              >{{ error }}<br></span>
            </b-form-group>
          </b-col>

          <p id="component-form-tags"></p>
          <p id="component-form-categories"></p>

          <b-col
            sm="12"
            v-if="updateCompany && !isClient"
            id="companyTags"
          >
            <TagsComponent
              accessoriesType="tags"
              :modelWithTags="company"
              :propTags="company.tags"
              modelType="companies"
              :title="$t('form.tags')"
              :senToApi="true"
            ></TagsComponent>
          </b-col>

          <b-col
            sm="12"
            v-if="updateCompany && !isClient"
          >
            <CategoriesComponent
              accessoriesType="categories"
              :modelWithCategories="company"
              :propCategories="company.categories"
              modelType="companies"
              :title="$t('form.categories')"
              :senToApi="true"
            ></CategoriesComponent>
          </b-col>
          <!--          <b-col
            sm="12"
            v-if="updateCompany && !isClient"
          >
            <nuxt-link :to="{ name: 'subjekt-referencni-projekt___cs', params: {id: updateCompany.id} }">
              <b-button
                class="btn-transition btn-hover-shine custom-sm"
                variant="primary"
                type="submit"
                size="sm"
              >
                {{$t('menu.ref_project_create') }}
              </b-button>
            </nuxt-link>
          </b-col>-->

          <b-col
            sm="12"
            v-if="!isConsultant"
          >
            <b-form-group
              id="description-group"
              label-for="company_description"
              :label="$t('form.description')"
            >
              <b-form-textarea
                id="company_description"
                v-model="description"
                v-bind:placeholder="$t('form.description')"
              >
              </b-form-textarea>
              <span
                class="text-danger"
                v-for="(error, index) in objectError.description"
                :key="index"
              >{{ error }}<br></span>
            </b-form-group>
          </b-col>
          <b-col
            sm="12"
            class="d-flex justify-content-center mb-5 mt-3"
          >
            <b-button
              class="btn-transition btn-hover-shine custom-lg"
              v-if="updateCompany"
              variant="primary"
              type="submit"
              size="lg"
            >
              {{ isConsultant ? $t('form.button.save') : $t('form.button.update') }}
            </b-button>
            <b-button
              v-else
              class="btn-transition btn-hover-shine custom-lg"
              variant="primary"
              type="submit"
              size="lg"
            >
              {{ $t('form.button.create') }}
            </b-button>
          </b-col>
        </b-row>
      </form>
    </div>
    <LoaderOverlay :showLoader="showLoader"></LoaderOverlay>
  </div>
</template>

<script>
import { mapActions, mapMutations, mapState, mapGetters } from "vuex";
import LoaderOverlay from "~/components/LoaderOverlay.vue";
import TagsComponent from "~/components/features/TagsComponent.vue";
import CategoriesComponent from "~/components/features/CategoriesComponent.vue";
import debounce from "debounce";
import { faLightbulb } from "@fortawesome/free-solid-svg-icons";
import { library } from "@fortawesome/fontawesome-svg-core";
library.add(faLightbulb);

export default {
  mounted() {
    //this.addToCompany({role: 'CONSULTANT'});
  },
  components: {
    LoaderOverlay,
    TagsComponent,
    CategoriesComponent,
  },
  props: ["updateCompany"],
  data() {
    return {
      new_company: {},
      radioFilter: "CONSULTANT",
      radioFilterOptions: [
        {
          text: this.$t("company.roles.consultant"),
          value: "CONSULTANT",
          selected: true,
        },
        { text: this.$t("company.roles.supplier"), value: "SUPPLIER" },
        { text: this.$t("company.roles.client"), value: "CLIENT" },
      ],
      radioUpdateOptions: [
        {
          text: this.$t("company.roles.consultant"),
          value: "CONSULTANT",
          disabled: true,
        },
        {
          text: this.$t("company.roles.supplier"),
          value: "SUPPLIER",
          disabled: true,
        },
        {
          text: this.$t("company.roles.client"),
          value: "CLIENT",
          disabled: true,
        },
      ],
      objectValidator: {
        reg_number: {
          name: "reg_number",
          rules: [
            /*'required'*/
          ],
        },
        name: {
          name: "name",
          rules: ["required"],
        },
      },
      showLoader: false,
    };
  },
  computed: {
    ...mapGetters({
      isClient: "user/isClient",
      isSupplier: "user/isSupplier",
      isConsultant: "user/isConsultant",
    }),
    ...mapState({
      company: (state) => state.companies.company,
      objectError: (state) => state.errors.objectError,
    }),
    city: {
      set(city) {
        this.addToCompany({ city });
      },
      get() {
        return this.company.city;
      },
    },
    street: {
      set(street) {
        this.addToCompany({ street });
      },
      get() {
        return this.company.street;
      },
    },
    street_number: {
      set(street_number) {
        this.addToCompany({ street_number });
      },
      get() {
        return this.company.street_number;
      },
    },
    zip: {
      set(zip) {
        this.addToCompany({ zip });
      },
      get() {
        return this.company.zip;
      },
    },
    dic: {
      set(dic) {
        this.addToCompany({ dic });
      },
      get() {
        return this.company.dic;
      },
    },
    name: {
      set(name) {
        this.addToCompany({ name });
      },
      get() {
        if (this.company.first_name) {
          return (
            this.company.first_name +
            (this.company.last_name ? this.company.last_name : "")
          );
        }
        return this.company.name;
      },
    },
    description: {
      set(description) {
        this.addToCompany({ description });
      },
      get() {
        return this.company.description;
      },
    },
    email: {
      set(email) {
        this.addToCompany({ email });
      },
      get() {
        return this.company.email;
      },
    },
    phone: {
      set(phone) {
        this.addToCompany({ phone });
      },
      get() {
        return this.company.phone;
      },
    },
    web: {
      set(web) {
        this.addToCompany({ web });
      },
      get() {
        return this.company.web;
      },
    },
    reg_number: {
      set(reg_number) {
        this.addToCompany({ reg_number });
      },
      get() {
        return this.company.reg_number;
      },
    },
    role: {
      set(role) {
        this.addToCompany({ role });
      },
      get() {
        return this.company.role || this.radioFilter;
      },
    },
  },
  methods: {
    changeRadioFilter() {},
    ...mapActions("companies", {
      uploadCompanyImage: "uploadCompanyImage",
      getCompanyByICO: "getCompanyByICO",
      updateAPICompany: "updateCompany",
      createAPICompany: "createCompany",
    }),
    ...mapActions("errors", {
      inputValidate: "validate",
    }),
    ...mapMutations("companies", {
      addToCompany: "addToCompany",
    }),
    async setImage() {
      const image = this.$refs.image.files[0];
      let formData = new FormData();
      formData.append("image", image);

      const data = {
        formData: formData,
        companyId: this.company.id,
      };
      this.uploadCompanyImage(data);
    },
    validate(input) {
      const data = {
        name: input,
        objectData: this.company,
        objectValidator: this.objectValidator,
      };
      this.inputValidate(data);
    },
    async LoadCompanyByIco(ico) {
      //console.log('LoadCompanyByIco', ico)
      if (ico === undefined) {
        this.$toast.error("IČO není vyplněné");
        return;
      }
      this.showLoader = true;
      await this.getCompanyByICO(ico);
      this.showLoader = false;
    },
    debounceRegNumberInput: debounce(async function (e) {
      //console.log({e}, this.reg_number)
      if (!this.reg_number?.trim()) return;
      await this.getCompanyByICO(this.reg_number.trim());
    }, 500),
    handleCompanyForm() {
      if (this.updateCompany) {
        this.updateAPICompany(this.company);
      } else {
        this.createAPICompany(this.company);
      }
    },
  },
};
</script>

<style lang="scss">
.nav-pills {
  .nav-item {
    .nav-link {
      transition: all ease-in-out 0.3s;
      height: 100%;
      a:hover {
        background-color: $cyan;
        color: $white !important;
      }

      > svg {
        width: 58px;
        display: inline-block;
        font-size: 22px;
      }
    }
  }
}
</style>