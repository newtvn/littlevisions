<template>
    <BaseModal id="composition-helper-modal">
        <template v-slot:header>
            <div class="center-container">

                <div class="helper-title">
                    <p class="helper-title">{{ helper.helper_title }}</p>
                </div>
           
            </div>
        </template>

        <template v-slot:body>

            <div class="center-container">
                <div class="helper-description">
                    <AvatarSpeak :text="helper.helper_text" />
                </div>

                <div class="helper-container row">
                    <div class="helper-card">
                        <p class="helper-info-text">
                            {{ helper.original_narrative }}
                        </p>
                    </div>

                    <div class="arrow-separator">
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M5 12H19M19 12L13 6M19 12L13 18" stroke="#000000" stroke-width="2"
                                stroke-linecap="round" stroke-linejoin="round" />
                        </svg>
                    </div>
                    <div class="helper-card creative">
                        <p class="helper-info-text">
                            {{ helper.creative_text }}
                        </p>
                    </div>
                </div>
            </div>
        </template>
        <template v-slot:footer>
            <!-- The footer -->
        </template>
    </BaseModal>
</template>
<script>
import BaseModal from '@/components/BaseModal.vue';
import AvatarSpeak from '@/components/AvatarSpeak.vue';
export default {
    components: {
        BaseModal, AvatarSpeak,
    },
    props: {
        helper: {
            type: Object,
            required: true
        }
    }
}
</script>