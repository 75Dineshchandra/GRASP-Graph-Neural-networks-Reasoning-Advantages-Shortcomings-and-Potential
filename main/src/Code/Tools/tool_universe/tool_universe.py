"""from test.test_tool_drug_ingredients import run_tool_demo as run_tool_1
from test.test_tool_Adverse_Reactions import run_tool_demo as run_tool_2
from test.test_tool_Warnings import run_tool_demo as run_tool_3
from test.test_tool_Dosage_and_Storage import run_tool_demo as run_tool_4

if __name__ == "__main__":
    print("==== Running tool test for active ingredient info ====\n")
    run_tool_1()

    print("\n==== Running tool test for adverse reactions (side effects) ====\n")
    run_tool_2()

    print("\n==== Running tool test for warnings ====\n")
    run_tool_3()

    print("\n==== Running tool test for dosage and storage instructions ====\n")
    run_tool_4()"""

#%%
# main.py

# main.py

# IMPORTANT:
# 1. Create a directory named 'test' in the same location as this main.py file.
# 2. Save all the 'test_tool_*.py' files provided into the 'test' directory.
# 3. Ensure 'tooluniverse' is installed in your Python environment (`pip install tooluniverse`).
# 4. Run this script from its parent directory: `python main.py`.

# Existing FDA Tools (from the provided main.py)
from test.test_tool_drug_ingredients import run_tool_demo as run_tool_1
from test.test_tool_Adverse_Reactions import run_tool_demo as run_tool_2
from test.test_tool_Warnings import run_tool_demo as run_tool_3
from test.test_tool_Dosage_and_Storage import run_tool_demo as run_tool_4

# Existing OpenTargets Tools (from the provided main.py)
from test.test_tool_OpenTargets_get_drug_withdrawn_blackbox_status_by_chemblId import run_tool_demo as run_tool_11
from test.test_tool_OpenTargets_search_category_counts_by_query_string import run_tool_demo as run_tool_12
from test.test_tool_OpenTargets_get_disease_id_description_by_name import run_tool_demo as run_tool_13
from test.test_tool_OpenTargets_get_drug_id_description_by_name import run_tool_demo as run_tool_14
from test.test_tool_OpenTargets_get_drug_chembId_by_generic_name import run_tool_demo as run_tool_15
from test.test_tool_OpenTargets_get_drug_indications_by_chemblId import run_tool_demo as run_tool_16
from test.test_tool_OpenTargets_get_target_gene_ontology_by_ensemblID import run_tool_demo as run_tool_17
from test.test_tool_OpenTargets_get_target_homologues_by_ensemblID import run_tool_demo as run_tool_18
from test.test_tool_OpenTargets_get_target_safety_profile_by_ensemblID import run_tool_demo as run_tool_19
from test.test_tool_OpenTargets_get_biological_mouse_models_by_ensemblID import run_tool_demo as run_tool_20

from test.test_tool_OpenTargets_get_associated_targets_by_disease_efoId import run_tool_demo as run_tool_ot_fda_1 # Renamed to avoid clash
from test.test_tool_OpenTargets_get_diseases_phenotypes_by_target_ensembl import run_tool_demo as run_tool_ot_fda_2 # Renamed to avoid clash
from test.test_tool_OpenTargets_target_disease_evidence import run_tool_demo as run_tool_ot_fda_3 # Renamed to avoid clash
from test.test_tool_OpenTargets_get_drug_warnings_by_chemblId import run_tool_demo as run_tool_ot_fda_4 # Renamed to avoid clash
from test.test_tool_OpenTargets_get_drug_mechanisms_of_action_by_chemblId import run_tool_demo as run_tool_ot_fda_5 # Renamed to avoid clash
from test.test_tool_OpenTargets_get_associated_drugs_by_disease_efoId import run_tool_demo as run_tool_ot_fda_6 # Renamed to avoid clash
from test.test_tool_OpenTargets_get_similar_entities_by_disease_efoId import run_tool_demo as run_tool_ot_fda_7 # Renamed to avoid clash
from test.test_tool_OpenTargets_get_similar_entities_by_drug_chemblId import run_tool_demo as run_tool_ot_fda_8 # Renamed to avoid clash
from test.test_tool_OpenTargets_get_similar_entities_by_target_ensemblID import run_tool_demo as run_tool_ot_fda_9 # Renamed to avoid clash
from test.test_tool_OpenTargets_get_associated_phenotypes_by_disease_efoId import run_tool_demo as run_tool_ot_fda_10 # Renamed to avoid clash

from test.test_tool_OT_get_target_genomic_location_by_ensemblID import run_tool_demo as run_tool_21
from test.test_tool_OT_get_target_subcellular_locations_by_ensemblID import run_tool_demo as run_tool_22
from test.test_tool_OT_get_target_synonyms_by_ensemblID import run_tool_demo as run_tool_23
from test.test_tool_OT_get_target_tractability_by_ensemblID import run_tool_demo as run_tool_24
from test.test_tool_OT_get_target_classes_by_ensemblID import run_tool_demo as run_tool_25
from test.test_tool_OT_get_target_enabling_packages_by_ensemblID import run_tool_demo as run_tool_26
from test.test_tool_OT_get_target_interactions_by_ensemblID import run_tool_demo as run_tool_27
from test.test_tool_OT_get_disease_ancestors_parents_by_efoId import run_tool_demo as run_tool_28
from test.test_tool_OT_get_disease_descendants_children_by_efoId import run_tool_demo as run_tool_29
from test.test_tool_OT_get_disease_locations_by_efoId import run_tool_demo as run_tool_30

from test.test_tool_OT_get_disease_synonyms_by_efoId import run_tool_demo as run_tool_31
from test.test_tool_OT_get_disease_description_by_efoId import run_tool_demo as run_tool_32
from test.test_tool_OT_get_disease_therapeutic_areas_by_efoId import run_tool_demo as run_tool_33
from test.test_tool_OT_get_drug_adverse_events_by_chemblId import run_tool_demo as run_tool_34
from test.test_tool_OT_get_known_drugs_by_drug_chemblId import run_tool_demo as run_tool_35
from test.test_tool_OT_get_parent_child_molecules_by_drug_chembl_ID import run_tool_demo as run_tool_36
from test.test_tool_OT_get_approved_indications_by_drug_chemblId import run_tool_demo as run_tool_37
from test.test_tool_OT_get_drug_synonyms_by_chemblId import run_tool_demo as run_tool_39
from test.test_tool_OT_get_drug_trade_names_by_chemblId import run_tool_demo as run_tool_40

from test.test_tool_OT_get_drug_approval_status_by_chemblId import run_tool_demo as run_tool_41
from test.test_tool_OT_get_chemical_probes_by_target_ensemblID import run_tool_demo as run_tool_42
from test.test_tool_OT_drug_pharmacogenomics_data import run_tool_demo as run_tool_43
from test.test_tool_OT_get_associated_drugs_by_target_ensemblID import run_tool_demo as run_tool_44
from test.test_tool_OT_get_associated_diseases_by_drug_chemblId import run_tool_demo as run_tool_45
from test.test_tool_OT_get_associated_targets_by_drug_chemblId import run_tool_demo as run_tool_46
from test.test_tool_OT_multi_entity_search_by_query_string import run_tool_demo as run_tool_47
from test.test_tool_OT_get_gene_ontology_terms_by_goID import run_tool_demo as run_tool_48
from test.test_tool_OT_get_target_constraint_info_by_ensemblID import run_tool_demo as run_tool_49
from test.test_tool_OT_get_publications_by_disease_efoId import run_tool_demo as run_tool_50

from test.test_tool_OT_get_publications_by_target_ensemblID import run_tool_demo as run_tool_51
from test.test_tool_OT_get_publications_by_drug_chemblId import run_tool_demo as run_tool_52
from test.test_tool_OT_get_target_id_description_by_name import run_tool_demo as run_tool_53
from test.test_tool_FDA_get_active_ingredient_info_by_drug_name import run_tool_demo as run_tool_54
from test.test_tool_FDA_get_dosage_and_storage_information_by_drug_name import run_tool_demo as run_tool_55
from test.test_tool_FDA_get_drug_names_by_abuse_info import run_tool_demo as run_tool_56
from test.test_tool_FDA_get_abuse_info_by_drug_name import run_tool_demo as run_tool_57
from test.test_tool_FDA_get_drug_names_by_accessories import run_tool_demo as run_tool_58
from test.test_tool_FDA_get_accessories_info_by_drug_name import run_tool_demo as run_tool_59
from test.test_tool_FDA_get_drug_names_by_active_ingredient import run_tool_demo as run_tool_60

from test.test_tool_FDA_get_manufacturer_name_NDC_number_by_drug_name import run_tool_demo as run_tool_61
from test.test_tool_FDA_get_drug_names_by_application_number_NDC_number import run_tool_demo as run_tool_62
from test.test_tool_FDA_get_drug_name_by_adverse_reaction import run_tool_demo as run_tool_63
from test.test_tool_FDA_get_adverse_reactions_by_drug_name import run_tool_demo as run_tool_64
from test.test_tool_FDA_get_drug_names_by_alarm import run_tool_demo as run_tool_65
from test.test_tool_FDA_get_alarms_by_drug_name import run_tool_demo as run_tool_66
from test.test_tool_FDA_get_drug_names_by_animal_pharmacology_info import run_tool_demo as run_tool_67
from test.test_tool_FDA_get_animal_pharmacology_info_by_drug_name import run_tool_demo as run_tool_68
from test.test_tool_FDA_get_drug_name_by_info_on_conditions_for_doctor_consultation import run_tool_demo as run_tool_69
from test.test_tool_FDA_get_info_on_conditions_for_doctor_consultation_by_drug_name import run_tool_demo as run_tool_70

from test.test_tool_FDA_get_drug_names_by_consulting_doctor_pharmacist_info import run_tool_demo as run_tool_71
from test.test_tool_FDA_get_info_on_consulting_doctor_pharmacist_by_drug_name import run_tool_demo as run_tool_72
from test.test_tool_FDA_get_drug_names_by_assembly_installation_info import run_tool_demo as run_tool_73
from test.test_tool_FDA_get_assembly_installation_info_by_drug_name import run_tool_demo as run_tool_74
from test.test_tool_FDA_get_drug_names_by_boxed_warning import run_tool_demo as run_tool_75
from test.test_tool_FDA_get_boxed_warning_info_by_drug_name import run_tool_demo as run_tool_76
from test.test_tool_FDA_get_drug_name_by_calibration_instructions import run_tool_demo as run_tool_77
from test.test_tool_FDA_get_calibration_instructions_by_drug_name import run_tool_demo as run_tool_78
from test.test_tool_FDA_get_drugs_by_carcinogenic_mutagenic_fertility import run_tool_demo as run_tool_79
from test.test_tool_FDA_get_carcinogenic_mutagenic_fertility_by_drug_name import run_tool_demo as run_tool_80

from test.test_tool_FDA_get_drug_name_by_SPL_ID import run_tool_demo as run_tool_81
from test.test_tool_FDA_get_drug_names_by_clinical_pharmacology import run_tool_demo as run_tool_82
from test.test_tool_FDA_get_clinical_pharmacology_by_drug_name import run_tool_demo as run_tool_83
from test.test_tool_FDA_get_drug_names_by_clinical_studies import run_tool_demo as run_tool_84
from test.test_tool_FDA_get_clinical_studies_info_by_drug_name import run_tool_demo as run_tool_85
from test.test_tool_FDA_get_drug_names_by_contraindications import run_tool_demo as run_tool_86
from test.test_tool_FDA_get_contraindications_by_drug_name import run_tool_demo as run_tool_87
from test.test_tool_FDA_get_drug_names_by_controlled_substance_DEA_schedule import run_tool_demo as run_tool_88
from test.test_tool_FDA_get_controlled_substance_DEA_schedule_info_by_drug_name import run_tool_demo as run_tool_89
from test.test_tool_FDA_get_drug_name_by_dependence_info import run_tool_demo as run_tool_90

from test.test_tool_FDA_get_dependence_info_by_drug_name import run_tool_demo as run_tool_91
from test.test_tool_FDA_get_drug_names_by_disposal_info import run_tool_demo as run_tool_92
from test.test_tool_FDA_get_disposal_info_by_drug_name import run_tool_demo as run_tool_93
from test.test_tool_FDA_get_drug_name_by_dosage_info import run_tool_demo as run_tool_94
from test.test_tool_FDA_get_drug_names_by_dosage_forms_and_strengths_info import run_tool_demo as run_tool_95
from test.test_tool_FDA_get_dosage_forms_and_strengths_by_drug_name import run_tool_demo as run_tool_96
from test.test_tool_FDA_get_drug_names_by_abuse_dependence_info import run_tool_demo as run_tool_97
from test.test_tool_FDA_get_abuse_dependence_info_by_drug_name import run_tool_demo as run_tool_98
from test.test_tool_FDA_get_drug_names_by_lab_test_interference import run_tool_demo as run_tool_99
from test.test_tool_FDA_get_lab_test_interference_info_by_drug_name import run_tool_demo as run_tool_100

from test.test_tool_FDA_get_drug_names_by_drug_interactions import run_tool_demo as run_tool_101
from test.test_tool_FDA_get_drug_interactions_by_drug_name import run_tool_demo as run_tool_102
from test.test_tool_FDA_get_drug_names_by_effective_time import run_tool_demo as run_tool_103
from test.test_tool_FDA_get_effective_time_by_drug_name import run_tool_demo as run_tool_104
from test.test_tool_FDA_get_drug_name_by_environmental_warning import run_tool_demo as run_tool_105
from test.test_tool_FDA_get_environmental_warning_by_drug_name import run_tool_demo as run_tool_106
from test.test_tool_FDA_get_drug_names_by_food_safety_warnings import run_tool_demo as run_tool_107
from test.test_tool_FDA_get_drug_names_by_general_precautions import run_tool_demo as run_tool_108
from test.test_tool_FDA_get_general_precautions_by_drug_name import run_tool_demo as run_tool_109
from test.test_tool_FDA_get_drug_names_by_geriatric_use import run_tool_demo as run_tool_110

# APPENDED TOOLS START HERE

# FDA Tools (from the first list provided in the initial prompt)
from test.test_tool_FDA_get_geriatric_use_info_by_drug_name import run_tool_demo as run_tool_fda_111
from test.test_tool_FDA_get_dear_health_care_provider_letter_info_by_drug_name import run_tool_demo as run_tool_fda_112 # (not working)
from test.test_tool_FDA_get_drug_names_by_dear_health_care_provider_letter_info import run_tool_demo as run_tool_fda_113
from test.test_tool_FDA_get_drug_names_by_health_claim import run_tool_demo as run_tool_fda_114
from test.test_tool_FDA_get_health_claims_by_drug_name import run_tool_demo as run_tool_fda_115
from test.test_tool_FDA_get_drug_name_by_document_id import run_tool_demo as run_tool_fda_116
from test.test_tool_FDA_get_document_id_by_drug_name import run_tool_demo as run_tool_fda_117
from test.test_tool_FDA_get_drug_name_by_inactive_ingredient import run_tool_demo as run_tool_fda_118
from test.test_tool_FDA_get_inactive_ingredient_info_by_drug_name import run_tool_demo as run_tool_fda_119
from test.test_tool_FDA_get_drug_names_by_indication import run_tool_demo as run_tool_fda_120

from test.test_tool_FDA_get_indications_by_drug_name import run_tool_demo as run_tool_fda_121
from test.test_tool_FDA_get_drug_names_by_information_for_owners_or_caregivers import run_tool_demo as run_tool_fda_122
from test.test_tool_FDA_get_information_for_owners_or_caregivers_by_drug_name import run_tool_demo as run_tool_fda_123
from test.test_tool_FDA_get_info_for_patients_by_drug_name import run_tool_demo as run_tool_fda_124
from test.test_tool_FDA_get_drug_names_by_instructions_for_use import run_tool_demo as run_tool_fda_125
from test.test_tool_FDA_get_instructions_for_use_by_drug_name import run_tool_demo as run_tool_fda_126
from test.test_tool_FDA_retrieve_drug_name_by_device_use import run_tool_demo as run_tool_fda_127 # (not working)
from test.test_tool_FDA_retrieve_device_use_by_drug_name import run_tool_demo as run_tool_fda_128 # (not working)
from test.test_tool_FDA_get_drug_names_by_child_safety_info import run_tool_demo as run_tool_fda_129
from test.test_tool_FDA_get_child_safety_info_by_drug_name import run_tool_demo as run_tool_fda_130

from test.test_tool_FDA_get_drug_name_by_labor_and_delivery_info import run_tool_demo as run_tool_fda_131
from test.test_tool_FDA_get_labor_and_delivery_info_by_drug_name import run_tool_demo as run_tool_fda_132
from test.test_tool_FDA_get_drug_names_by_lab_tests import run_tool_demo as run_tool_fda_133
from test.test_tool_FDA_get_lab_tests_by_drug_name import run_tool_demo as run_tool_fda_134
from test.test_tool_FDA_get_mechanism_of_action_by_drug_name import run_tool_demo as run_tool_fda_135
from test.test_tool_FDA_get_drug_names_by_mechanism_of_action import run_tool_demo as run_tool_fda_136
from test.test_tool_FDA_get_drug_name_by_microbiology import run_tool_demo as run_tool_fda_137
from test.test_tool_FDA_get_microbiology_info_by_drug_name import run_tool_demo as run_tool_fda_138
from test.test_tool_FDA_get_drug_names_by_nonclinical_toxicology_info import run_tool_demo as run_tool_fda_139
from test.test_tool_FDA_get_nonclinical_toxicology_info_by_drug_name import run_tool_demo as run_tool_fda_140

from test.test_tool_FDA_get_drug_names_by_nonteratogenic_effects import run_tool_demo as run_tool_fda_141
from test.test_tool_FDA_get_nonteratogenic_effects_by_drug_name import run_tool_demo as run_tool_fda_142
from test.test_tool_FDA_get_drug_names_by_info_for_nursing_mothers import run_tool_demo as run_tool_fda_143
from test.test_tool_FDA_get_info_for_nursing_mothers_by_drug_name import run_tool_demo as run_tool_fda_144
from test.test_tool_FDA_get_drug_name_by_other_safety_info import run_tool_demo as run_tool_fda_145
from test.test_tool_FDA_get_other_safety_info_by_drug_name import run_tool_demo as run_tool_fda_146
from test.test_tool_FDA_get_drug_names_by_overdosage_info import run_tool_demo as run_tool_fda_147
from test.test_tool_FDA_get_overdosage_info_by_drug_name import run_tool_demo as run_tool_fda_148
from test.test_tool_FDA_get_drug_name_by_principal_display_panel import run_tool_demo as run_tool_fda_149
from test.test_tool_FDA_get_principal_display_panel_by_drug_name import run_tool_demo as run_tool_fda_150

from test.test_tool_FDA_retrieve_drug_names_by_patient_medication_info import run_tool_demo as run_tool_fda_151
from test.test_tool_FDA_retrieve_patient_medication_info_by_drug_name import run_tool_demo as run_tool_fda_152
from test.test_tool_FDA_get_drug_names_by_pediatric_use import run_tool_demo as run_tool_fda_153
from test.test_tool_FDA_get_pediatric_use_info_by_drug_name import run_tool_demo as run_tool_fda_154
from test.test_tool_FDA_get_drug_name_by_pharmacodynamics import run_tool_demo as run_tool_fda_155
from test.test_tool_FDA_get_pharmacodynamics_by_drug_name import run_tool_demo as run_tool_fda_156
from test.test_tool_FDA_get_drug_name_by_pharmacogenomics import run_tool_demo as run_tool_fda_157
from test.test_tool_FDA_get_pharmacogenomics_info_by_drug_name import run_tool_demo as run_tool_fda_158
from test.test_tool_FDA_get_drug_names_by_pharmacokinetics import run_tool_demo as run_tool_fda_159
from test.test_tool_FDA_get_pharmacokinetics_by_drug_name import run_tool_demo as run_tool_fda_160

from test.test_tool_FDA_get_drug_name_by_precautions import run_tool_demo as run_tool_fda_161
from test.test_tool_FDA_get_precautions_by_drug_name import run_tool_demo as run_tool_fda_162
from test.test_tool_FDA_get_drug_names_by_pregnancy_effects_info import run_tool_demo as run_tool_fda_163
from test.test_tool_FDA_get_pregnancy_effects_info_by_drug_name import run_tool_demo as run_tool_fda_164
from test.test_tool_FDA_get_drug_name_by_pregnancy_or_breastfeeding_info import run_tool_demo as run_tool_fda_165
from test.test_tool_FDA_get_pregnancy_or_breastfeeding_info_by_drug_name import run_tool_demo as run_tool_fda_166
from test.test_tool_FDA_get_contact_for_questions_info_by_drug_name import run_tool_demo as run_tool_fda_167
from test.test_tool_FDA_get_recent_changes_by_drug_name import run_tool_demo as run_tool_fda_168
from test.test_tool_FDA_get_drug_name_by_reference import run_tool_demo as run_tool_fda_169
from test.test_tool_FDA_get_reference_info_by_drug_name import run_tool_demo as run_tool_fda_170

from test.test_tool_FDA_get_drug_names_by_residue_warning import run_tool_demo as run_tool_fda_171 # (not working)
from test.test_tool_FDA_get_residue_warning_by_drug_name import run_tool_demo as run_tool_fda_172 # (not working)
from test.test_tool_FDA_get_drug_names_by_risk import run_tool_demo as run_tool_fda_173
from test.test_tool_FDA_get_risk_info_by_drug_name import run_tool_demo as run_tool_fda_174
from test.test_tool_FDA_get_drug_names_by_route import run_tool_demo as run_tool_fda_175
from test.test_tool_FDA_get_route_info_by_drug_name import run_tool_demo as run_tool_fda_176
from test.test_tool_FDA_get_drug_names_by_safe_handling_warning import run_tool_demo as run_tool_fda_177
from test.test_tool_FDA_get_safe_handling_warnings_by_drug_name import run_tool_demo as run_tool_fda_178
from test.test_tool_FDA_get_drug_name_by_set_id import run_tool_demo as run_tool_fda_179
from test.test_tool_FDA_get_drug_names_by_spl_indexing_data_elements import run_tool_demo as run_tool_fda_180

from test.test_tool_FDA_get_spl_indexing_data_elements_by_drug_name import run_tool_demo as run_tool_fda_181
from test.test_tool_FDA_get_drug_names_by_medication_guide import run_tool_demo as run_tool_fda_182
from test.test_tool_FDA_get_medication_guide_info_by_drug_name import run_tool_demo as run_tool_fda_183
from test.test_tool_FDA_get_drug_name_from_patient_package_insert import run_tool_demo as run_tool_fda_184
from test.test_tool_FDA_get_patient_package_insert_from_drug_name import run_tool_demo as run_tool_fda_185
from test.test_tool_FDA_get_drug_names_by_ingredient import run_tool_demo as run_tool_fda_186
from test.test_tool_FDA_get_ingredients_by_drug_name import run_tool_demo as run_tool_fda_187
from test.test_tool_FDA_get_spl_unclassified_section_by_drug_name import run_tool_demo as run_tool_fda_188
from test.test_tool_FDA_get_drug_name_by_stop_use_info import run_tool_demo as run_tool_fda_189
from test.test_tool_FDA_get_stop_use_info_by_drug_name import run_tool_demo as run_tool_fda_190

from test.test_tool_FDA_get_drug_name_by_storage_and_handling_info import run_tool_demo as run_tool_fda_191
from test.test_tool_FDA_get_storage_and_handling_info_by_drug_name import run_tool_demo as run_tool_fda_192
from test.test_tool_FDA_get_drug_names_by_safety_summary import run_tool_demo as run_tool_fda_193
from test.test_tool_FDA_get_safety_summary_by_drug_name import run_tool_demo as run_tool_fda_194
from test.test_tool_FDA_get_drug_names_by_teratogenic_effects import run_tool_demo as run_tool_fda_195
from test.test_tool_FDA_get_teratogenic_effects_by_drug_name import run_tool_demo as run_tool_fda_196
from test.test_tool_FDA_get_drug_names_by_population_use import run_tool_demo as run_tool_fda_197
from test.test_tool_FDA_get_population_use_info_by_drug_name import run_tool_demo as run_tool_fda_198
from test.test_tool_FDA_get_user_safety_warning_by_drug_names import run_tool_demo as run_tool_fda_199
from test.test_tool_FDA_get_drug_names_by_user_safety_warning import run_tool_demo as run_tool_fda_200

from test.test_tool_FDA_get_drug_name_by_warnings import run_tool_demo as run_tool_fda_201
from test.test_tool_FDA_get_warnings_by_drug_name import run_tool_demo as run_tool_fda_202
from test.test_tool_FDA_get_warnings_and_cautions_by_drug_name import run_tool_demo as run_tool_fda_203
from test.test_tool_FDA_get_drug_names_by_warnings_and_cautions import run_tool_demo as run_tool_fda_204
from test.test_tool_FDA_get_when_using_info import run_tool_demo as run_tool_fda_205
from test.test_tool_FDA_get_brand_name_generic_name import run_tool_demo as run_tool_fda_206
from test.test_tool_FDA_get_do_not_use_info_by_drug_name import run_tool_demo as run_tool_fda_207
from test.test_tool_FDA_get_purpose_info_by_drug_name import run_tool_demo as run_tool_fda_208
from test.test_tool_FDA_get_drug_generic_name import run_tool_demo as run_tool_fda_209


# Special Tools
from tooluniverse import Finish as run_tool_special_1
from tooluniverse import Tool_RAG as run_tool_special_2
from tooluniverse import CallAgent as run_tool_special_3
from tooluniverse import get_joint_associated_diseases_by_HPO_ID_list as run_tool_special_4
from tooluniverse import get_phenotype_by_HPO_ID as run_tool_special_5
from tooluniverse import get_HPO_ID_by_phenotype as run_tool_special_6

if __name__ == "__main__":
    print("==== Running existing FDA tool tests ====\n")
    run_tool_1()
    run_tool_2()
    run_tool_3()
    run_tool_4()
    run_tool_54()
    run_tool_55()
    run_tool_56()
    run_tool_57()
    run_tool_58()
    run_tool_59()
    run_tool_60()
    run_tool_61()
    run_tool_62()
    run_tool_63()
    run_tool_64()
    run_tool_65()
    run_tool_66()
    run_tool_67()
    run_tool_68()
    run_tool_69()
    run_tool_70()
    run_tool_71()
    run_tool_72()
    run_tool_73()
    run_tool_74()
    run_tool_75()
    run_tool_76()
    run_tool_77()
    run_tool_78()
    run_tool_79()
    run_tool_80()
    run_tool_81()
    run_tool_82()
    run_tool_83()
    run_tool_84()
    run_tool_85()
    run_tool_86()
    run_tool_87()
    run_tool_88()
    run_tool_89()
    run_tool_90()
    run_tool_91()
    run_tool_92()
    run_tool_93()
    run_tool_94()
    run_tool_95()
    run_tool_96()
    run_tool_97()
    run_tool_98()
    run_tool_99()
    run_tool_100()
    run_tool_101()
    run_tool_102()
    run_tool_103()
    run_tool_104()
    run_tool_105()
    run_tool_106()
    run_tool_107()
    run_tool_108()
    run_tool_109()
    run_tool_110()

    print("\n==== Running existing OpenTargets tool tests ====\n")
    run_tool_11()
    run_tool_12()
    run_tool_13()
    run_tool_14()
    run_tool_15()
    run_tool_16()
    run_tool_17()
    run_tool_18()
    run_tool_19()
    run_tool_20()
    run_tool_ot_fda_1() # Renamed alias
    run_tool_ot_fda_2() # Renamed alias
    run_tool_ot_fda_3() # Renamed alias
    run_tool_ot_fda_4() # Renamed alias
    run_tool_ot_fda_5() # Renamed alias
    run_tool_ot_fda_6() # Renamed alias
    run_tool_ot_fda_7() # Renamed alias
    run_tool_ot_fda_8() # Renamed alias
    run_tool_ot_fda_9() # Renamed alias
    run_tool_ot_fda_10() # Renamed alias
    run_tool_21()
    run_tool_22()
    run_tool_23()
    run_tool_24()
    run_tool_25()
    run_tool_26()
    run_tool_27()
    run_tool_28()
    run_tool_29()
    run_tool_30()
    run_tool_31()
    run_tool_32()
    run_tool_33()
    run_tool_34()
    run_tool_35()
    run_tool_36()
    run_tool_37()
    # The original file had run_tool_38 commented out. Including it here if the intention is to add ALL tools.
    # If test_tool_OT_get_drug_description_by_chemblId.py exists and is meant to be run:
    # from test.test_tool_OT_get_drug_description_by_chemblId import run_tool_demo as run_tool_38
    # print("\n==== Running tool test for OT_get_drug_description_by_chemblId ====\n")
    # run_tool_38()
    run_tool_39()
    run_tool_40()
    run_tool_41()
    run_tool_42()
    run_tool_43()
    run_tool_44()
    run_tool_45()
    run_tool_46()
    run_tool_47()
    run_tool_48()
    run_tool_49()
    run_tool_50()
    run_tool_51()
    run_tool_52()
    run_tool_53()

    # APPENDED TOOLS EXECUTION START HERE

    print("\n==== Running appended FDA tool tests ====\n")
    print("==== Running tool test for FDA_get_geriatric_use_info_by_drug_name ====\n")
    run_tool_fda_111()
    print("==== Running tool test for (not working) FDA_get_dear_health_care_provider_letter_info_by_drug_name ====\n")
    run_tool_fda_112()
    print("==== Running tool test for FDA_get_drug_names_by_dear_health_care_provider_letter_info ====\n")
    run_tool_fda_113()
    print("==== Running tool test for FDA_get_drug_names_by_health_claim ====\n")
    run_tool_fda_114()
    print("==== Running tool test for FDA_get_health_claims_by_drug_name ====\n")
    run_tool_fda_115()
    print("==== Running tool test for FDA_get_drug_name_by_document_id ====\n")
    run_tool_fda_116()
    print("==== Running tool test for FDA_get_document_id_by_drug_name ====\n")
    run_tool_fda_117()
    print("==== Running tool test for FDA_get_drug_name_by_inactive_ingredient ====\n")
    run_tool_fda_118()
    print("==== Running tool test for FDA_get_inactive_ingredient_info_by_drug_name ====\n")
    run_tool_fda_119()
    print("==== Running tool test for FDA_get_drug_names_by_indication ====\n")
    run_tool_fda_120()
    print("==== Running tool test for FDA_get_indications_by_drug_name ====\n")
    run_tool_fda_121()
    print("==== Running tool test for FDA_get_drug_names_by_information_for_owners_or_caregivers ====\n")
    run_tool_fda_122()
    print("==== Running tool test for FDA_get_information_for_owners_or_caregivers_by_drug_name ====\n")
    run_tool_fda_123()
    print("==== Running tool test for FDA_get_info_for_patients_by_drug_name ====\n")
    run_tool_fda_124()
    print("==== Running tool test for FDA_get_drug_names_by_instructions_for_use ====\n")
    run_tool_fda_125()
    print("==== Running tool test for FDA_get_instructions_for_use_by_drug_name ====\n")
    run_tool_fda_126()
    print("==== Running tool test for (not working) FDA_retrieve_drug_name_by_device_use ====\n")
    run_tool_fda_127()
    print("==== Running tool test for (not working) FDA_retrieve_device_use_by_drug_name ====\n")
    run_tool_fda_128()
    print("==== Running tool test for FDA_get_drug_names_by_child_safety_info ====\n")
    run_tool_fda_129()
    print("==== Running tool test for FDA_get_child_safety_info_by_drug_name ====\n")
    run_tool_fda_130()
    print("==== Running tool test for FDA_get_drug_name_by_labor_and_delivery_info ====\n")
    run_tool_fda_131()
    print("==== Running tool test for FDA_get_labor_and_delivery_info_by_drug_name ====\n")
    run_tool_fda_132()
    print("==== Running tool test for FDA_get_drug_names_by_lab_tests ====\n")
    run_tool_fda_133()
    print("==== Running tool test for FDA_get_lab_tests_by_drug_name ====\n")
    run_tool_fda_134()
    print("==== Running tool test for FDA_get_mechanism_of_action_by_drug_name ====\n")
    run_tool_fda_135()
    print("==== Running tool test for FDA_get_drug_names_by_mechanism_of_action ====\n")
    run_tool_fda_136()
    print("==== Running tool test for FDA_get_drug_name_by_microbiology ====\n")
    run_tool_fda_137()
    print("==== Running tool test for FDA_get_microbiology_info_by_drug_name ====\n")
    run_tool_fda_138()
    print("==== Running tool test for FDA_get_drug_names_by_nonclinical_toxicology_info ====\n")
    run_tool_fda_139()
    print("==== Running tool test for FDA_get_nonclinical_toxicology_info_by_drug_name ====\n")
    run_tool_fda_140()
    print("==== Running tool test for FDA_get_drug_names_by_nonteratogenic_effects ====\n")
    run_tool_fda_141()
    print("==== Running tool test for FDA_get_nonteratogenic_effects_by_drug_name ====\n")
    run_tool_fda_142()
    print("==== Running tool test for FDA_get_drug_names_by_info_for_nursing_mothers ====\n")
    run_tool_fda_143()
    print("==== Running tool test for FDA_get_info_for_nursing_mothers_by_drug_name ====\n")
    run_tool_fda_144()
    print("==== Running tool test for FDA_get_drug_name_by_other_safety_info ====\n")
    run_tool_fda_145()
    print("==== Running tool test for FDA_get_other_safety_info_by_drug_name ====\n")
    run_tool_fda_146()
    print("==== Running tool test for FDA_get_drug_names_by_overdosage_info ====\n")
    run_tool_fda_147()
    print("==== Running tool test for FDA_get_overdosage_info_by_drug_name ====\n")
    run_tool_fda_148()
    print("==== Running tool test for FDA_get_drug_name_by_principal_display_panel ====\n")
    run_tool_fda_149()
    print("==== Running tool test for FDA_get_principal_display_panel_by_drug_name ====\n")
    run_tool_fda_150()
    print("==== Running tool test for FDA_retrieve_drug_names_by_patient_medication_info ====\n")
    run_tool_fda_151()
    print("==== Running tool test for FDA_retrieve_patient_medication_info_by_drug_name ====\n")
    run_tool_fda_152()
    print("==== Running tool test for FDA_get_drug_names_by_pediatric_use ====\n")
    run_tool_fda_153()
    print("==== Running tool test for FDA_get_pediatric_use_info_by_drug_name ====\n")
    run_tool_fda_154()
    print("==== Running tool test for FDA_get_drug_name_by_pharmacodynamics ====\n")
    run_tool_fda_155()
    print("==== Running tool test for FDA_get_pharmacodynamics_by_drug_name ====\n")
    run_tool_fda_156()
    print("==== Running tool test for FDA_get_drug_name_by_pharmacogenomics ====\n")
    run_tool_fda_157()
    print("==== Running tool test for FDA_get_pharmacogenomics_info_by_drug_name ====\n")
    run_tool_fda_158()
    print("==== Running tool test for FDA_get_drug_names_by_pharmacokinetics ====\n")
    run_tool_fda_159()
    print("==== Running tool test for FDA_get_pharmacokinetics_by_drug_name ====\n")
    run_tool_fda_160()
    print("==== Running tool test for FDA_get_drug_name_by_precautions ====\n")
    run_tool_fda_161()
    print("==== Running tool test for FDA_get_precautions_by_drug_name ====\n")
    run_tool_fda_162()
    print("==== Running tool test for FDA_get_drug_names_by_pregnancy_effects_info ====\n")
    run_tool_fda_163()
    print("==== Running tool test for FDA_get_pregnancy_effects_info_by_drug_name ====\n")
    run_tool_fda_164()
    print("==== Running tool test for FDA_get_drug_name_by_pregnancy_or_breastfeeding_info ====\n")
    run_tool_fda_165()
    print("==== Running tool test for FDA_get_pregnancy_or_breastfeeding_info_by_drug_name ====\n")
    run_tool_fda_166()
    print("==== Running tool test for FDA_get_contact_for_questions_info_by_drug_name ====\n")
    run_tool_fda_167()
    print("==== Running tool test for FDA_get_recent_changes_by_drug_name ====\n")
    run_tool_fda_168()
    print("==== Running tool test for FDA_get_drug_name_by_reference ====\n")
    run_tool_fda_169()
    print("==== Running tool test for FDA_get_reference_info_by_drug_name ====\n")
    run_tool_fda_170()
    print("==== Running tool test for (not working) FDA_get_drug_names_by_residue_warning ====\n")
    run_tool_fda_171()
    print("==== Running tool test for (not working) FDA_get_residue_warning_by_drug_name ====\n")
    run_tool_fda_172()
    print("==== Running tool test for FDA_get_drug_names_by_risk ====\n")
    run_tool_fda_173()
    print("==== Running tool test for FDA_get_risk_info_by_drug_name ====\n")
    run_tool_fda_174()
    print("==== Running tool test for FDA_get_drug_names_by_route ====\n")
    run_tool_fda_175()
    print("==== Running tool test for FDA_get_route_info_by_drug_name ====\n")
    run_tool_fda_176()
    print("==== Running tool test for FDA_get_drug_names_by_safe_handling_warning ====\n")
    run_tool_fda_177()
    print("==== Running tool test for FDA_get_safe_handling_warnings_by_drug_name ====\n")
    run_tool_fda_178()
    print("==== Running tool test for FDA_get_drug_name_by_set_id ====\n")
    run_tool_fda_179()
    print("==== Running tool test for FDA_get_drug_names_by_spl_indexing_data_elements ====\n")
    run_tool_fda_180()
    print("==== Running tool test for FDA_get_spl_indexing_data_elements_by_drug_name ====\n")
    run_tool_fda_181()
    print("==== Running tool test for FDA_get_drug_names_by_medication_guide ====\n")
    run_tool_fda_182()
    print("==== Running tool test for FDA_get_medication_guide_info_by_drug_name ====\n")
    run_tool_fda_183()
    print("==== Running tool test for FDA_get_drug_name_from_patient_package_insert ====\n")
    run_tool_fda_184()
    print("==== Running tool test for FDA_get_patient_package_insert_from_drug_name ====\n")
    run_tool_fda_185()
    print("==== Running tool test for FDA_get_drug_names_by_ingredient ====\n")
    run_tool_fda_186()
    print("==== Running tool test for FDA_get_ingredients_by_drug_name ====\n")
    run_tool_fda_187()
    print("==== Running tool test for FDA_get_spl_unclassified_section_by_drug_name ====\n")
    run_tool_fda_188()
    print("==== Running tool test for FDA_get_drug_name_by_stop_use_info ====\n")
    run_tool_fda_189()
    print("==== Running tool test for FDA_get_stop_use_info_by_drug_name ====\n")
    run_tool_fda_190()
    print("==== Running tool test for FDA_get_drug_name_by_storage_and_handling_info ====\n")
    run_tool_fda_191()
    print("==== Running tool test for FDA_get_storage_and_handling_info_by_drug_name ====\n")
    run_tool_fda_192()
    print("==== Running tool test for FDA_get_drug_names_by_safety_summary ====\n")
    run_tool_fda_193()
    print("==== Running tool test for FDA_get_safety_summary_by_drug_name ====\n")
    run_tool_fda_194()
    print("==== Running tool test for FDA_get_drug_names_by_teratogenic_effects ====\n")
    run_tool_fda_195()
    print("==== Running tool test for FDA_get_teratogenic_effects_by_drug_name ====\n")
    run_tool_fda_196()
    print("==== Running tool test for FDA_get_drug_names_by_population_use ====\n")
    run_tool_fda_197()
    print("==== Running tool test for FDA_get_population_use_info_by_drug_name ====\n")
    run_tool_fda_198()
    print("==== Running tool test for FDA_get_user_safety_warning_by_drug_names ====\n")
    run_tool_fda_199()
    print("==== Running tool test for FDA_get_drug_names_by_user_safety_warning ====\n")
    run_tool_fda_200()
    print("==== Running tool test for FDA_get_drug_name_by_warnings ====\n")
    run_tool_fda_201()
    print("==== Running tool test for FDA_get_warnings_by_drug_name ====\n")
    run_tool_fda_202()
    print("==== Running tool test for FDA_get_warnings_and_cautions_by_drug_name ====\n")
    run_tool_fda_203()
    print("==== Running tool test for FDA_get_drug_names_by_warnings_and_cautions ====\n")
    run_tool_fda_204()
    print("==== Running tool test for FDA_get_when_using_info ====\n")
    run_tool_fda_205()
    print("==== Running tool test for FDA_get_brand_name_generic_name ====\n")
    run_tool_fda_206()
    print("==== Running tool test for FDA_get_do_not_use_info_by_drug_name ====\n")
    run_tool_fda_207()
    print("==== Running tool test for FDA_get_purpose_info_by_drug_name ====\n")
    run_tool_fda_208()
    print("==== Running tool test for FDA_get_drug_generic_name ====\n")
    run_tool_fda_209()

    print("\n--- Running Special Tool Demos (Note: These may require specific environments or inputs) ---")
    # The special tools often require specific parameters or a running environment
    # that is not typically set up in a simple script. They are included for completeness
    # but may not execute successfully without further configuration.
    try:
        run_tool_special_1() # Finish
        print("Finish tool executed (if applicable).")
    except Exception as e:
        print(f"Error executing Finish tool: {e}")

    try:
        run_tool_special_2() # Tool_RAG
        print("Tool_RAG executed (if applicable).")
    except Exception as e:
        print(f"Error executing Tool_RAG: {e}")

    try:
        run_tool_special_3() # CallAgent
        print("CallAgent tool executed (if applicable).")
    except Exception as e:
        print(f"Error executing CallAgent: {e}")

    try:
        # Example: You'd need a list of HPO IDs here.
        # run_tool_special_4(hpo_id_list=["HP:0000118"])
        print("get_joint_associated_diseases_by_HPO_ID_list - call not executed, requires HPO IDs.")
    except Exception as e:
        print(f"Error with get_joint_associated_diseases_by_HPO_ID_list: {e}")

    try:
        # Example: You'd need an HPO ID here.
        # run_tool_special_5(hpo_id="HP:0000118")
        print("get_phenotype_by_HPO_ID - call not executed, requires HPO ID.")
    except Exception as e:
        print(f"Error with get_phenotype_by_HPO_ID: {e}")

    try:
        # Example: You'd need a phenotype name here.
        # run_tool_special_6(phenotype_name="Abnormality of body height")
        print("get_HPO_ID_by_phenotype - call not executed, requires phenotype name.")
    except Exception as e:
        print(f"Error with get_HPO_ID_by_phenotype: {e}")