from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



from django.utils.encoding import python_2_unicode_compatible





class Program(models.Model):
    name = models.CharField(max_length=120)


    def __str__(self):
        return self.name
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others')

)
ANSWER_CHOICES=(
     ('Strongly Disagree','Strongly Disagree'),
     ('Disagree','Disagree'),
     ('Neutral','Neutral'),
     ('Agree','Agree'),
     ('Strongly Agree', 'Strongly Agree'),
)


class ProgramFeedbackForm(models.Model):
    intern_name = models.CharField(max_length=30,blank=True,null=True)

    date_posted = models.DateTimeField(default=timezone.now)
    program = models.ForeignKey(Program,blank=True,null=True, on_delete= models.CASCADE)
    gender = models.CharField(max_length=20,blank=True,null=True,choices=GENDER_CHOICES )
    Overall_my_impression_of_this_course_was_excellent = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_course_objectives_were_clearly_stated_and_used_understandable_terms=models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    This_course_met_the_defined_objectives = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Both_the_facility_and_equipment_used_met_all_needs_of_the_course = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_course_materials_were_both_useful_and_easy_to_follow  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_instructor_demonstrated_thorough_knowledge_and_understanding_of_the_topic = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_instructor_presented_information_in_a_clear_understandable_and_professional_manner= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_amount_of_time_scheduled_for_this_course_was_exactly_what_was_needed_to_meet_the_objectives= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    This_course_relates_directly_to_my_current_job_responsibilities = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_would_recommend_this_course_to_other_teammates  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    details = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.intern_name

class SixThinkingHats_SelfEvaluation(models.Model):

     intern_name = models.CharField(max_length=40)
     email = models.EmailField()
     I_try_to_formulate_a_clear_definition_of_the_problem = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_of_the_goal_and_outcome_of_the_problem_I_am_facing = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_plan_to_figure_out_the_most_effective_method_to_proceed_from_the_initial_problem = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_try_to_organize_and_arrange_my_thinking_to_help_move_me_beyond_my_present_circumstances = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_try_to_figure_out_what_I_know_about_the_problem = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_try_to_figure_out_what_I_dont_know_about_the_problem = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_of_how_I_will_go_about_acquiring_the_facts_stats_and_data_that_will_help_me_resolve_this_problem = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_figure_out_potential_solutions_exist_based_on_the_facts_stats_and_data_I_have_collected  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_consider_what_my_feelings_tell_me_about_the_choice_I_am_about_to_make = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_of_better_ways_to_solve_a_problem_based_on_my_feelings = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_if_the_solution_is_the_right_one_based_on_my_intuition = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_try_to_find_fatal_flaws_in_a_problem = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_consider_the_potential_risks_and_consequences_associated_with_the_problem = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_if_I_have_the_necessary_resources_skills_and_support_to_solve_the_problem_or_not =  models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_of_how_I_can_logically_and_realistically_make_the_solution_work = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_of_the_positive_outcomes_that_could_result_from_an_action = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_of_the_long_term_benefits_of_an_action= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_of_the_alternative_possibilities_that_could_exist_when_considering_a_decision = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_think_of_different_ways_I_could_approach_the_problem = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
     I_try_to_think_of_an_out_of_the_box_solution = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )

     def __str__(self):
         return self.intern_name




class Six_hats_Writeup(models.Model):
    intern_name = models.CharField(max_length=40)
    email=models.EmailField()
    Write_a_brief_write_up_about_how_you_effectively_used_Six_Thinking_Hats_technique_to_solve_a_problem_at_the_workplace = models.TextField()

    def __str__(self):
        return self.intern_name


class Man_eff_SelfEvaluation(models.Model):
    intern_name = models.CharField(max_length= 40)
    email = models.EmailField()
    I_identify_what_and_when_to_delegate_a_task_or_role_that_will_be_motivating_for_your_employees = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_give_constructive_behavior_based_feedback = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_practise_active_listening = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_assess_conflict_situations_and_apply_the_most_appropriate_modes = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_practice_overall_team_management_and_effective_leadership_skills = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_identify_when_is_the_best_time_to_tell_vs_ask_in_a_conversation = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_know_the_types_of_questions_to_use_to_dig_deeper_into_a_conversation = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )

    def __str__(self):
        return self.intern_name

class Man_eff_RelationshipWithManager(models.Model):

    intern_name = models.CharField(max_length= 40)
    email = models.EmailField()
    gender = models.CharField(max_length=20,blank=True,null=True,choices=GENDER_CHOICES )
    Name_of_your_Manager = models.CharField(max_length=50)
    My_manager_understands_my_problems_and_needs =  models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    My_manager_recognizes_my_potential = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Regardless_of_how_much_power_he_she_has_built_into_his_her_position_my_manager_would_be_personally_inclined_to_use_his_her_power_to_help_me_solve_problems_in_my_work = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    My_supervisor_has_enough_confidence_in_me_that_he_she_would_defend_and_justify_my_decisions_if_I_were_not_present_to_do_so = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_can_count_on_my_manager_to_bail_me_out_at_his_her_expense_when_I_really_need_it = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    My_manager_has_enough_confidence_in_me_that_he_she_would_defend_and_justiy_my_decision_if_I_am_not_present_to_do_so = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_know_how_satisfied_my_manager_is_with_what_I_do = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )

    def __str__(self):
        return self.intern_name


class Man_eff_Employee_Engagement(models.Model):

    intern_name = models.CharField(max_length= 40)
    email = models.EmailField()
    gender = models.CharField(max_length=20,blank=True,null=True,choices=GENDER_CHOICES )
    Name_of_your_Manager = models.CharField(max_length=50)
    I_know_what_is_expected_of_me_at_work = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_am_willing_to_really_push_myself_to_reach_challenging_work_goals = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_have_the_opportunity_to_do_what_I_do_best_every_day = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    My_supervisor_or_someone_at_work_seems_to_care_about_my_personal_development = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_am_enthusiastic_about_providing_a_high_quality_product_or_service = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_am_always_willing_to_go_the_extra_mile_in_order_to_do_my_job_well = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Trying_to_constantly_improve_my_job_performance_is_very_important_to_me = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    My_job_is_a_source_of_personal_pride_for_me = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_receive_recognition_or_praise_for_doing_good_work = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    My_opinions_seem_to_count_at_work = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Someone_has_talked_to_me_about_my_progress_in_the_past_6_months = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )

    def __str__(self):
        return self.intern_name

class Together_win_Self_Assessment(models.Model):
    intern_name = models.CharField(max_length= 40)
    email = models.EmailField()
    gender = models.CharField(max_length=20,blank=True,null=True,choices=GENDER_CHOICES )
    My_team_has_a_meaningful_and_shared_purpose= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_clearly_understand_my_role_within_the_team= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Team_problem_solving_results_in_effective_solutions= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_appreciate_the_unique_capabilities_of_my_team_members= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_take_personal_responsibility_for_the_effectiveness_of_my_team = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Working_on_my_team_aspires_me_to_do_my_best= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_have_the_skills_I_need_to_do_my_job_for_the_team_effectively = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    My_team_sets_and_meets_challenging_goals= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    When_an_individuals_role_changes_I_make_an_intentional_effort_to_clarify_it_for_everyone_on_the_team= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_address_and_resolve_issues_quickly = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_am_open_and_honest_with_the_communication_in_my_group= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_take_initiative_to_resolve_issues_between_the_team_members_without_involving_the_team_leader= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_have_a_strong_sense_of_accomplishment_regarding_my_work= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_always_ask_myself_How_can_we_do_better_tomorrow_what_we_did_today= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    As_a_part_of_my_team_I_always_produce_strong_measurable_results= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_avoid_duplication_of_efforts_and_make_sure_that_everyone_is_clear_about_who_is_doing_what = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    My_team_has_mechanisms_in_place_to_monitor_its_results= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_trust_the_members_of_my_team = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_spend_very_little_time_complaining_about_things_I_cannot_control= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_frequently_go_beyond_what_is_required_and_do_not_hesitate_to_take_initiative = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    As_a_team_we_are_continually_working_to_improve_key_performance_indicators = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_make_sure_my_work_helps_the_organization_achieve_its_goals = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    When_team_members_roles_change_Specific_plans_are_implemented_to_help_them_assume_their_new_responsibilities = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_work_with_a_great_deal_of_flexibility_so_that_I_can_adapt_to_changing_needs= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_help_other_team_members_deal_with_problems_or_resolve_issues= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_seek_and_give_other_team_members_with_constructive_feedback = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    As_a_team_we_work_to_attract_and_retain_top_performers= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    We_work_to_ensure_that_we_are_using_the_best_practices = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_mission_and_goals_of_my_team_are_well_aligned_with_the_organizations_mission_and_goals= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Overlapping_or_shared_tasks_and_responsibilities_do_not_create_problems_for_team_members= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    When_we_choose_consensus_decision_making_we_do_it_effectively = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_am_able_to_work_through_differences_of_opinion_without_damaging_relationships = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_am_sure_about_what_is_expected_of_me_and_take_pride_in_a_job_well_done= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_am_excited_about_the_contribution_it_is_making_to_the_organizations_competitive_viability = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_embrace_continuous_improvement_as_a_way_of_life= models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )

    def __str__(self):
        return self.intern_name






class Together_win_Peer_Review(models.Model):
    intern_name = models.CharField(max_length= 40)
    email = models.EmailField()
    gender = models.CharField(max_length=20,blank=True,null=True,choices=GENDER_CHOICES )
    Name_of_your_Teammate = models.CharField(max_length=100)
    Teammate_clearly_understands_the_purpose_of_our_team=  models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Teammate_openly_expresses_ideas_and_opinions=  models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Teammate_is_able_to_make_thoughtful_decisions_that_all_team_members_support =  models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Teammate_trusts_and_respects_other_team_members=  models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Teammate_expresses_disagreements_constructively=  models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Teammate_willingly_take_on_new_responsibilities=  models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Teammate_follow_through_on_decisions_and_action_items =  models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Teammate_has_the_necessary_skills_to_carry_out_his_work=  models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    Teammate_frequently_goes_beyond_what_is_required_and_does_not_hesitate_to_take_initiative=  models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )

    def __str__(self):
        return self.intern_name

class BusinessCommuniction_Self_Assessment(models.Model):
    intern_name = models.CharField(max_length= 40)
    email = models.EmailField()
    gender = models.CharField(max_length=20,blank=True,null=True,choices=GENDER_CHOICES )
    I_am_very_clear_in_my_mind_about_what_I_want_to_say = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_communicate_while_keeping_in_mind_the_environment_or_the_need_of_the_receiver  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    The_contents_of_my_message_are_brief_and_clear = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_keep_in_mind_the_need_and_interest_of_the_receiver_before_speaking  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_try_to_gauge_the_face_of_the_receiver_during_face_to_face_communication_as_an_attempt_to_get_feedback = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_look_at_the_speaker_while_he_or_she_is_talking  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_listen_to_people_who_say_things_I_disagree_with_or_dont_want_to_hear  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_ask_for_clarification_if_I_am_unclear_about_what_is_being_said = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_pay_attention_when_not_interested_in_what_the_person_is_saying_or_find_the_topic_too_complex  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_dont_have_any_doubts_on_any_questions_that_have_already_been_answered_by_the_speaker  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_listen_to_the_main_ideas_or_the_whole_picture_not_only_the_facts  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_do_not_use_excess_words_during_writing  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_present_all_the_necessary_facts_while_sending_written_communication = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_use_positive_words_and_phrases_instead_of_negative_ones = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_avoid_vague_expressions_in_my_writing_to_maintain_clarity  = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_avoid_the_use_of_jargon_in_my_writing = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_carefully_proof_read_the_important_contents_of_my_data = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_make_sure_that_the_statement_says_what_I_intend_it_to_say = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )

    def __str__(self):
        return self.intern_name

class Presentation_Self_Assessment(models.Model):
    intern_name = models.CharField(max_length= 40)
    email = models.EmailField()
    gender = models.CharField(max_length=20,blank=True,null=True,choices=GENDER_CHOICES )
    Before_preparing_the_content_I_make_sure_that_I_am_clear_about_the_objectives_of_the_session = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_ensure_that_all_equipment_is_functioning_properly_at_the_venue_before_starting_my_presentation = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_make_a_thorough_research_about_the_topic_and_prepare_content_that_is_interesting_and_useful =models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_identify_my_audience_before_I_start_preparing_for_my_presentation = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_consider_immediate_needs_and_pain_points_and_obstacles_of_my_audience_regarding_the_topic_I_will_present=models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_can_gauge_the_level_of_interest_of_my_audience_on_the_topic_being_presented =models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_make_sure_that_the_contents_are_relevant_and_logical_and_meet_the_needs_of_participants=models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_make_sure_that_the_content_or_information_I_am_giving_is_appropriate_to_the_culture_and_sentiments_of_the_audience=models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_am_very_clear_in_the_statements_that_I_use=models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_use_the_appropriate_font_size_so_that_the_on_screen_text_is_readable=models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_ensure_that_the_presentation_has_a_proper_flow_clarity_and_the_right_amount_of_information=models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_use_suitable_pictures_and_charts_and_figures_to_enhance_the_effectiveness_of_the_presentation=models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_use_relevant_stories_and_analogies_and_examples_and_humor_etc_during_the_presentation=models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_maintain_eye_contact_and_try_to_connect_with_the_participants_during_the_presentation=models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_take_care_of_my_voice_modulation_and_tone_and_pitch_and_language_during_the_presentation=models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )
    I_make_sure_that_I_give_a_worthwhile_summary_and_make_a_convincing_conclusion = models.CharField(max_length=25,blank=True,null=True,choices=ANSWER_CHOICES )

    def __str__(self):
        return self.intern_name









LEVEL_CHOICES = (
     ('warning', 'Warning'),
     ('error', 'Error'),
     ('success', 'Success'),
     ('info', 'Info'),
)

class Announcement(models.Model):
    """
    Model to hold global announcements
    """
    body = models.TextField(blank=False)
    display = models.BooleanField(default=False)
    level = models.CharField(max_length=7,
                choices=LEVEL_CHOICES, default='info')

    def __unicode__(self):
        return self.body[:50]
