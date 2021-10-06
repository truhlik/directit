<template>
  <div>
    <b-row>
      <b-col md="6">
        <b-form-group label-for="firstName">
          <b-form-input
            id="firstName"
            type="text"
            v-model="user.first_name"
            required
            :placeholder="`${this.$t('auth.enterFirstName')}...`"
            :state="getValidator().first_name.state"
            @change="checkValidity()"
          />
        </b-form-group>
      </b-col>
      <b-col md="6">
        <b-form-group label-for="lastName">
          <b-form-input
            id="lastName"
            type="text"
            v-model="user.last_name"
            required
            :placeholder="`${this.$t('auth.enterLastName')}...`"
            :state="getValidator().last_name.state"
            @change="checkValidity()"
          />
        </b-form-group>
      </b-col>
    </b-row>
    <b-form-group
      label-for="email"
      description="We'll never share your email with anyone else."
    >
      <b-form-input
        id="email"
        type="email"
        v-model="user.email"
        required
        :placeholder="`${this.$t('auth.enterEmail')}...`"
        :state="getValidator().email.state"
        @change="checkValidity()"
      />
    </b-form-group>
    <b-form-group
      label-for="phone"
      description="Neither your phone..."
    >
      <b-form-input
        id="phone"
        type="tel"
        v-model="user.phone"
        required
        :placeholder="`${this.$t('auth.enterPhone')}...`"
        :state="getValidator().phone.state"
        @change="checkValidity()"
      />
    </b-form-group>
    <div class="divider"/>
    <b-form-group>
      <b-form-checkbox v-model="isCompany" name="check-button" switch>
        {{ $t('auth.weAreCompany') }}
      </b-form-checkbox>
    </b-form-group>
    <b-form-group label-for="companyName" v-if="isCompany">
      <b-form-input
        id="companyName"
        type="text"
        v-model="user.title"
        :required="isCompany"
        :placeholder="`${this.$t('auth.enterCompanyName')}...`"
        :state="getValidator().title.state"
        @change="checkValidity()"
      />
    </b-form-group>
    <b-row>
      <b-col md="6">
        <b-form-group label-for="regNumber" v-if="isCompany">
          <b-form-input
            id="regNumber"
            type="text"
            v-model="user.company_id"
            :required="isCompany"
            :placeholder="`${this.$t('auth.enterReg')}...`"
            :state="getValidator().company_id.state"
            @change="checkValidity()"
          />
        </b-form-group>
      </b-col>
      <b-col md="6">
        <b-form-group label-for="vatNumber" v-if="isCompany">
          <b-form-input
            id="vatNumber"
            type="text"
            v-model="user.tax_id"
            :required="isCompany"
            :placeholder="`${this.$t('auth.enterVat')}...`"
            :state="getValidator().tax_id.state"
            @change="checkValidity()"
          />
        </b-form-group>
      </b-col>
    </b-row>
    <b-form-group label-for="wwwAddress" v-if="isCompany">
      <b-form-input
        id="wwwAddress"
        type="url"
        v-model="user.www"
        :placeholder="`${this.$t('auth.enterWww')}...`"
        :state="getValidator().www.state"
        @change="checkValidity()"
      />
    </b-form-group>
  </div>
</template>

<script>
  import { validateDummy, validateEmail, validateRequiredField, validateRequiredIfField } from "~/helpers/validators";

  export default {
    name: "RegisterForm",
    props: {
      user: {
        type: Object,
        required: true,
      }
    },
    data() {
      return {
        isCompany: false,
      }
    },
    methods: {
      checkValidity() {
        const validator = this.getValidator();
        for (let key in validator)
          if(validator[key].valid === false) {
            this.$emit('validationChange', false);
            return;
          }

        this.$emit('validationChange', true);
      },
      getValidator() {
        return {
          // first_name: validateRequiredField(this.user.first_name),
          // last_name: validateRequiredField(this.user.last_name),
          // email: validateEmail(this.user.email),
          // phone: validateDummy(this.user.phone),
          // title: validateRequiredIfField(this.user.title, this.isCompany),
          // company_id: validateRequiredIfField(this.user.company_id, this.isCompany),
          // tax_id: validateDummy(this.user.tax_id),
          // www: validateDummy(this.user.www)
        };
      },
    },
  }
</script>

<style scoped>

</style>
