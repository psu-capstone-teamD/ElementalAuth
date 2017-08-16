import unittest
from SchedulerController import SchedulerController


class MyTestCase(unittest.TestCase):
    def test_storebxffile_wrong_filename(self):
        schedControl = SchedulerController()
        data = "This is some data to put into s3"
        print(schedControl.storebxffile(1, data))

    def test_storebxffile_wrong_filetype(self):
        schedControl = SchedulerController()
        print(schedControl.storebxffile('afilename.xml', 1))

    def test_storelivefile_wrong_filename(self):
        schedControl = SchedulerController()
        data = "This is some data to put into s3"
        print(schedControl.storelivefile(1, data))

    def test_storelivefile_wrong_filetype(self):
        schedControl = SchedulerController()
        print(schedControl.storelivefile('afilename.xml', 1))

    def test_loadlivefile_wrong_filename(self):
        schedControl = SchedulerController()
        print(schedControl.loadLiveFile(1))

    def test_sendtolive_wrong_filename(self):
        schedControl = SchedulerController()
        print(schedControl.createLiveEvent(1))

    def test_inputxml_wrong_filetype(self):
        schedControl = SchedulerController()
        print(schedControl.inputxml(1))

    def test_inputxml_wrong_filetype_string(self):
        schedControl = SchedulerController()
        print(schedControl.inputxml(
            "<android.support.design.widget.AppBarLayout><android.support.v7.widget.Toolbar/></android.support.design.widget.AppBarLayout>"))

    def test_inputxml_is_filetype(self):
        schedControl = SchedulerController()
        data = "This is some data to put into s3"
        print(schedControl.inputxml(data))

    def test_updatelive_wrong_data(self):
        schedControl = SchedulerController()
        print(schedControl.updateLiveEvent(1))

    def test_updatelive_right_data(self):
        schedControl = SchedulerController()
        print(schedControl.updateLiveEvent(
            "<android.support.design.widget.AppBarLayout><android.support.v7.widget.Toolbar/></android.support.design.widget.AppBarLayout>"))

    def test_getlastuuid(self):
        schedControl = SchedulerController()
        print(schedControl.getLastUUID('<live_event href="/live_events/149" product="Elemental Conductor Live + Audio Normalization Package + Audio Package + Audio Decode Package" version="2.10.0.44452"><name>test_event</name><input><deblock_enable>Auto</deblock_enable><deblock_strength>0</deblock_strength><error_clear_time nil="true"/><failback_rule>immediately</failback_rule><hot_backup_pair>false</hot_backup_pair><input_label nil="true"/><loop_source>false</loop_source><no_psi>false</no_psi><order>1</order><service_name nil="true"/><service_provider_name nil="true"/><timecode_source>embedded</timecode_source><file_input><certificate_file nil="true"/><uri>https://s3-us-west-2.amazonaws.com/pdxteamdkrakatoa/KLM+Delft+blue+house+94+De+Oudheidkamer.mp4</uri></file_input><name>input_1</name><video_selector><color_space nil="true"/><order>1</order><program_id nil="true"/><name>input_1_video_selector_0</name></video_selector><audio_selector><default_selection>false</default_selection><order>1</order><program_selection>1</program_selection><selector_type nil="true"/><unwrap_smpte337>true</unwrap_smpte337><name>input_1_audio_selector_0</name></audio_selector></input><input><deblock_enable>Auto</deblock_enable><deblock_strength>0</deblock_strength><error_clear_time nil="true"/><failback_rule>immediately</failback_rule><hot_backup_pair>false</hot_backup_pair><input_label nil="true"/><loop_source>false</loop_source><no_psi>false</no_psi><order>2</order><service_name nil="true"/><service_provider_name nil="true"/><timecode_source>embedded</timecode_source><file_input><certificate_file nil="true"/><uri>https://s3-us-west-2.amazonaws.com/pdxteamdkrakatoa/IMG_0467.MOV</uri></file_input><name>input_2</name><video_selector><color_space nil="true"/><order>1</order><program_id nil="true"/><name>input_2_video_selector_0</name></video_selector><audio_selector><default_selection>false</default_selection><order>1</order><program_selection>1</program_selection><selector_type nil="true"/><unwrap_smpte337>true</unwrap_smpte337><name>input_2_audio_selector_0</name></audio_selector></input><loop_all_inputs>false</loop_all_inputs><timecode_config><require_initial_timecode>false</require_initial_timecode><source>embedded</source><sync_threshold nil="true"/></timecode_config><failure_rule><priority>50</priority><restart_on_failure>false</restart_on_failure><backup_rule/></failure_rule><ad_trigger>scte35_splice_insert</ad_trigger><ad_avail_offset>0</ad_avail_offset><ignore_web_delivery_allowed_flag>false</ignore_web_delivery_allowed_flag><ignore_no_regional_blackout_flag>false</ignore_no_regional_blackout_flag><low_latency_mode>false</low_latency_mode><initial_audio_gain>0</initial_audio_gain><avsync_enable>true</avsync_enable><avsync_pad_trim_audio>true</avsync_pad_trim_audio><user_data/><input_switch_buffer>0</input_switch_buffer><input_buffer_size>60</input_buffer_size><low_framerate_input>false</low_framerate_input><extract_sdt>false</extract_sdt><stream_assembly><name>stream_assembly_0</name><video_description><afd_signaling>None</afd_signaling><anti_alias>true</anti_alias><drop_frame_timecode>true</drop_frame_timecode><fixed_afd nil="true"/><force_cpu_encode>false</force_cpu_encode><height>320</height><insert_color_metadata>false</insert_color_metadata><respond_to_afd>None</respond_to_afd><sharpness>50</sharpness><stretch_to_output>false</stretch_to_output><timecode_passthrough>false</timecode_passthrough><vbi_passthrough>false</vbi_passthrough><width>480</width><h264_settings><adaptive_quantization>medium</adaptive_quantization><bitrate>5000000</bitrate><buf_fill_pct nil="true"/><buf_size nil="true"/><cabac>true</cabac><flicker_reduction>off</flicker_reduction><force_field_pictures>false</force_field_pictures><framerate_denominator nil="true"/><framerate_follow_source>true</framerate_follow_source><framerate_numerator nil="true"/><gop_b_reference>false</gop_b_reference><gop_closed_cadence>1</gop_closed_cadence><gop_markers>false</gop_markers><gop_num_b_frames>2</gop_num_b_frames><gop_size>90.0</gop_size><gop_size_units>frames</gop_size_units><interpolate_frc>false</interpolate_frc><look_ahead_rate_control>medium</look_ahead_rate_control><max_bitrate nil="true"/><max_qp nil="true"/><min_bitrate nil="true"/><min_buf_occ nil="true"/><min_i_interval>0</min_i_interval><min_qp nil="true"/><num_ref_frames>1</num_ref_frames><par_denominator nil="true"/><par_follow_source>true</par_follow_source><par_numerator nil="true"/><passes>1</passes><qp nil="true"/><repeat_pps>false</repeat_pps><rp2027_syntax>false</rp2027_syntax><scd>true</scd><sei_timecode>false</sei_timecode><slices>1</slices><slow_pal>false</slow_pal><softness nil="true"/><svq>0</svq><telecine>None</telecine><profile>Main</profile><rate_control_mode>CBR</rate_control_mode><gop_mode>fixed</gop_mode><interlace_mode>progressive</interlace_mode></h264_settings><selected_gpu nil="true"/><codec>h.264</codec></video_description><audio_description><audio_type>0</audio_type><follow_input_audio_type>true</follow_input_audio_type><follow_input_language_code>true</follow_input_language_code><language_code nil="true"/><order>1</order><stream_name nil="true"/><timecode_passthrough>false</timecode_passthrough><aac_settings><ad_broadcaster_mix>false</ad_broadcaster_mix><bitrate>96000</bitrate><coding_mode>2_0</coding_mode><latm_loas>false</latm_loas><mpeg2>false</mpeg2><sample_rate>48000</sample_rate><profile>LC</profile><rate_control_mode>CBR</rate_control_mode></aac_settings><codec>aac</codec></audio_description></stream_assembly><output_group><custom_name>udp_ts</custom_name><name nil="true"/><order>1</order><udp_group_settings><on_input_loss>drop_ts</on_input_loss><timed_metadata_id3_frame>PRIV</timed_metadata_id3_frame><timed_metadata_id3_period>10</timed_metadata_id3_period><name>udp_group_settings</name></udp_group_settings><type>udp_group_settings</type><output><arib_captions_passthrough>false</arib_captions_passthrough><description nil="true"/><ebif_passthrough>false</ebif_passthrough><extension>m2ts</extension><insert_amf_metadata>false</insert_amf_metadata><insert_private_metadata>false</insert_private_metadata><insert_scte35_esam>false</insert_scte35_esam><insert_timed_metadata>false</insert_timed_metadata><klv_passthrough>false</klv_passthrough><log_edit_points>false</log_edit_points><name_modifier nil="true"/><nielsen_id3_passthrough>false</nielsen_id3_passthrough><order>1</order><scte35_passthrough>false</scte35_passthrough><start_paused>false</start_paused><udp_settings><buffer_msec>1000</buffer_msec><max_ts_packet_count>7</max_ts_packet_count><mpts_membership>none</mpts_membership><destination><uri>udp://10.0.50.157:5901</uri></destination></udp_settings><m2ts_settings><arib>false</arib><audio_frames_per_pes>2</audio_frames_per_pes><bitrate>0</bitrate><drop_absent_streams>false</drop_absent_streams><dvb>false</dvb><es_rate>false</es_rate><null_packet_bitrate nil="true"/><pat_interval>100</pat_interval><pcr_every_pes>true</pcr_every_pes><pcr_period nil="true"/><pmt_interval>100</pmt_interval><program_num>1</program_num><scte35_pullup>0</scte35_pullup><segmentation_markers>none</segmentation_markers><segmentation_style>maintain_cadence</segmentation_style><segmentation_time nil="true"/><transport_stream_id nil="true"/><use_atsc_stream_type>false</use_atsc_stream_type><use_buffer_model>true</use_buffer_model><vbr>false</vbr><dvb_sdt_settings><output_sdt>sdt_follow</output_sdt><rep_interval>500</rep_interval><service_name/><service_provider_name/></dvb_sdt_settings><audio_pids>482-498</audio_pids><dvb_sub_pids>460-479</dvb_sub_pids><dvb_teletext_pid>499</dvb_teletext_pid><pmt_pid>480</pmt_pid><video_pid>481</video_pid></m2ts_settings><stream_assembly_name>stream_assembly_0</stream_assembly_name><container>m2ts</container></output></output_group></live_event>'))

    def test_getelapsed(self):
        schedControl = SchedulerController()
        print(schedControl.getElapsedInSeconds('<live_event href="/live_events/149" product="Elemental Conductor Live + Audio Normalization Package + Audio Package + Audio Decode Package" version="2.10.0.44452"><name>test_event</name><input><deblock_enable>Auto</deblock_enable><deblock_strength>0</deblock_strength><error_clear_time nil="true"/><failback_rule>immediately</failback_rule><hot_backup_pair>false</hot_backup_pair><input_label nil="true"/><loop_source>false</loop_source><no_psi>false</no_psi><order>1</order><service_name nil="true"/><service_provider_name nil="true"/><timecode_source>embedded</timecode_source><file_input><certificate_file nil="true"/><uri>https://s3-us-west-2.amazonaws.com/pdxteamdkrakatoa/KLM+Delft+blue+house+94+De+Oudheidkamer.mp4</uri></file_input><name>input_1</name><video_selector><color_space nil="true"/><order>1</order><program_id nil="true"/><name>input_1_video_selector_0</name></video_selector><audio_selector><default_selection>false</default_selection><order>1</order><program_selection>1</program_selection><selector_type nil="true"/><unwrap_smpte337>true</unwrap_smpte337><name>input_1_audio_selector_0</name></audio_selector></input><input><deblock_enable>Auto</deblock_enable><deblock_strength>0</deblock_strength><error_clear_time nil="true"/><failback_rule>immediately</failback_rule><hot_backup_pair>false</hot_backup_pair><input_label nil="true"/><loop_source>false</loop_source><no_psi>false</no_psi><order>2</order><service_name nil="true"/><service_provider_name nil="true"/><timecode_source>embedded</timecode_source><file_input><certificate_file nil="true"/><uri>https://s3-us-west-2.amazonaws.com/pdxteamdkrakatoa/IMG_0467.MOV</uri></file_input><name>input_2</name><video_selector><color_space nil="true"/><order>1</order><program_id nil="true"/><name>input_2_video_selector_0</name></video_selector><audio_selector><default_selection>false</default_selection><order>1</order><program_selection>1</program_selection><selector_type nil="true"/><unwrap_smpte337>true</unwrap_smpte337><name>input_2_audio_selector_0</name></audio_selector></input><loop_all_inputs>false</loop_all_inputs><timecode_config><require_initial_timecode>false</require_initial_timecode><source>embedded</source><sync_threshold nil="true"/></timecode_config><failure_rule><priority>50</priority><restart_on_failure>false</restart_on_failure><backup_rule/></failure_rule><ad_trigger>scte35_splice_insert</ad_trigger><ad_avail_offset>0</ad_avail_offset><ignore_web_delivery_allowed_flag>false</ignore_web_delivery_allowed_flag><ignore_no_regional_blackout_flag>false</ignore_no_regional_blackout_flag><low_latency_mode>false</low_latency_mode><initial_audio_gain>0</initial_audio_gain><avsync_enable>true</avsync_enable><avsync_pad_trim_audio>true</avsync_pad_trim_audio><user_data/><input_switch_buffer>0</input_switch_buffer><input_buffer_size>60</input_buffer_size><low_framerate_input>false</low_framerate_input><extract_sdt>false</extract_sdt><stream_assembly><name>stream_assembly_0</name><video_description><afd_signaling>None</afd_signaling><anti_alias>true</anti_alias><drop_frame_timecode>true</drop_frame_timecode><fixed_afd nil="true"/><force_cpu_encode>false</force_cpu_encode><height>320</height><insert_color_metadata>false</insert_color_metadata><respond_to_afd>None</respond_to_afd><sharpness>50</sharpness><stretch_to_output>false</stretch_to_output><timecode_passthrough>false</timecode_passthrough><vbi_passthrough>false</vbi_passthrough><width>480</width><h264_settings><adaptive_quantization>medium</adaptive_quantization><bitrate>5000000</bitrate><buf_fill_pct nil="true"/><buf_size nil="true"/><cabac>true</cabac><flicker_reduction>off</flicker_reduction><force_field_pictures>false</force_field_pictures><framerate_denominator nil="true"/><framerate_follow_source>true</framerate_follow_source><framerate_numerator nil="true"/><gop_b_reference>false</gop_b_reference><gop_closed_cadence>1</gop_closed_cadence><gop_markers>false</gop_markers><gop_num_b_frames>2</gop_num_b_frames><gop_size>90.0</gop_size><gop_size_units>frames</gop_size_units><interpolate_frc>false</interpolate_frc><look_ahead_rate_control>medium</look_ahead_rate_control><max_bitrate nil="true"/><max_qp nil="true"/><min_bitrate nil="true"/><min_buf_occ nil="true"/><min_i_interval>0</min_i_interval><min_qp nil="true"/><num_ref_frames>1</num_ref_frames><par_denominator nil="true"/><par_follow_source>true</par_follow_source><par_numerator nil="true"/><passes>1</passes><qp nil="true"/><repeat_pps>false</repeat_pps><rp2027_syntax>false</rp2027_syntax><scd>true</scd><sei_timecode>false</sei_timecode><slices>1</slices><slow_pal>false</slow_pal><softness nil="true"/><svq>0</svq><telecine>None</telecine><profile>Main</profile><rate_control_mode>CBR</rate_control_mode><gop_mode>fixed</gop_mode><interlace_mode>progressive</interlace_mode></h264_settings><selected_gpu nil="true"/><codec>h.264</codec></video_description><audio_description><audio_type>0</audio_type><follow_input_audio_type>true</follow_input_audio_type><follow_input_language_code>true</follow_input_language_code><language_code nil="true"/><order>1</order><stream_name nil="true"/><timecode_passthrough>false</timecode_passthrough><aac_settings><ad_broadcaster_mix>false</ad_broadcaster_mix><bitrate>96000</bitrate><coding_mode>2_0</coding_mode><latm_loas>false</latm_loas><mpeg2>false</mpeg2><sample_rate>48000</sample_rate><profile>LC</profile><rate_control_mode>CBR</rate_control_mode></aac_settings><codec>aac</codec></audio_description></stream_assembly><output_group><custom_name>udp_ts</custom_name><name nil="true"/><order>1</order><udp_group_settings><on_input_loss>drop_ts</on_input_loss><timed_metadata_id3_frame>PRIV</timed_metadata_id3_frame><timed_metadata_id3_period>10</timed_metadata_id3_period><name>udp_group_settings</name></udp_group_settings><type>udp_group_settings</type><output><arib_captions_passthrough>false</arib_captions_passthrough><description nil="true"/><ebif_passthrough>false</ebif_passthrough><extension>m2ts</extension><insert_amf_metadata>false</insert_amf_metadata><insert_private_metadata>false</insert_private_metadata><insert_scte35_esam>false</insert_scte35_esam><insert_timed_metadata>false</insert_timed_metadata><klv_passthrough>false</klv_passthrough><log_edit_points>false</log_edit_points><name_modifier nil="true"/><nielsen_id3_passthrough>false</nielsen_id3_passthrough><order>1</order><scte35_passthrough>false</scte35_passthrough><start_paused>false</start_paused><udp_settings><buffer_msec>1000</buffer_msec><max_ts_packet_count>7</max_ts_packet_count><mpts_membership>none</mpts_membership><destination><uri>udp://10.0.50.157:5901</uri></destination></udp_settings><m2ts_settings><arib>false</arib><audio_frames_per_pes>2</audio_frames_per_pes><bitrate>0</bitrate><drop_absent_streams>false</drop_absent_streams><dvb>false</dvb><es_rate>false</es_rate><null_packet_bitrate nil="true"/><pat_interval>100</pat_interval><pcr_every_pes>true</pcr_every_pes><pcr_period nil="true"/><pmt_interval>100</pmt_interval><program_num>1</program_num><scte35_pullup>0</scte35_pullup><segmentation_markers>none</segmentation_markers><segmentation_style>maintain_cadence</segmentation_style><segmentation_time nil="true"/><transport_stream_id nil="true"/><use_atsc_stream_type>false</use_atsc_stream_type><use_buffer_model>true</use_buffer_model><vbr>false</vbr><dvb_sdt_settings><output_sdt>sdt_follow</output_sdt><rep_interval>500</rep_interval><service_name/><service_provider_name/></dvb_sdt_settings><audio_pids>482-498</audio_pids><dvb_sub_pids>460-479</dvb_sub_pids><dvb_teletext_pid>499</dvb_teletext_pid><pmt_pid>480</pmt_pid><video_pid>481</video_pid></m2ts_settings><stream_assembly_name>stream_assembly_0</stream_assembly_name><container>m2ts</container></output></output_group></live_event>'))

    def test_getduration(self):
        schedControl = SchedulerController()
        print(schedControl.getElapsedInSeconds('<live_event href="/live_events/149" product="Elemental Conductor Live + Audio Normalization Package + Audio Package + Audio Decode Package" version="2.10.0.44452"><name>test_event</name><input><deblock_enable>Auto</deblock_enable><deblock_strength>0</deblock_strength><error_clear_time nil="true"/><failback_rule>immediately</failback_rule><hot_backup_pair>false</hot_backup_pair><input_label nil="true"/><loop_source>false</loop_source><no_psi>false</no_psi><order>1</order><service_name nil="true"/><service_provider_name nil="true"/><timecode_source>embedded</timecode_source><file_input><certificate_file nil="true"/><uri>https://s3-us-west-2.amazonaws.com/pdxteamdkrakatoa/KLM+Delft+blue+house+94+De+Oudheidkamer.mp4</uri></file_input><name>input_1</name><video_selector><color_space nil="true"/><order>1</order><program_id nil="true"/><name>input_1_video_selector_0</name></video_selector><audio_selector><default_selection>false</default_selection><order>1</order><program_selection>1</program_selection><selector_type nil="true"/><unwrap_smpte337>true</unwrap_smpte337><name>input_1_audio_selector_0</name></audio_selector></input><input><deblock_enable>Auto</deblock_enable><deblock_strength>0</deblock_strength><error_clear_time nil="true"/><failback_rule>immediately</failback_rule><hot_backup_pair>false</hot_backup_pair><input_label nil="true"/><loop_source>false</loop_source><no_psi>false</no_psi><order>2</order><service_name nil="true"/><service_provider_name nil="true"/><timecode_source>embedded</timecode_source><file_input><certificate_file nil="true"/><uri>https://s3-us-west-2.amazonaws.com/pdxteamdkrakatoa/IMG_0467.MOV</uri></file_input><name>input_2</name><video_selector><color_space nil="true"/><order>1</order><program_id nil="true"/><name>input_2_video_selector_0</name></video_selector><audio_selector><default_selection>false</default_selection><order>1</order><program_selection>1</program_selection><selector_type nil="true"/><unwrap_smpte337>true</unwrap_smpte337><name>input_2_audio_selector_0</name></audio_selector></input><loop_all_inputs>false</loop_all_inputs><timecode_config><require_initial_timecode>false</require_initial_timecode><source>embedded</source><sync_threshold nil="true"/></timecode_config><failure_rule><priority>50</priority><restart_on_failure>false</restart_on_failure><backup_rule/></failure_rule><ad_trigger>scte35_splice_insert</ad_trigger><ad_avail_offset>0</ad_avail_offset><ignore_web_delivery_allowed_flag>false</ignore_web_delivery_allowed_flag><ignore_no_regional_blackout_flag>false</ignore_no_regional_blackout_flag><low_latency_mode>false</low_latency_mode><initial_audio_gain>0</initial_audio_gain><avsync_enable>true</avsync_enable><avsync_pad_trim_audio>true</avsync_pad_trim_audio><user_data/><input_switch_buffer>0</input_switch_buffer><input_buffer_size>60</input_buffer_size><low_framerate_input>false</low_framerate_input><extract_sdt>false</extract_sdt><stream_assembly><name>stream_assembly_0</name><video_description><afd_signaling>None</afd_signaling><anti_alias>true</anti_alias><drop_frame_timecode>true</drop_frame_timecode><fixed_afd nil="true"/><force_cpu_encode>false</force_cpu_encode><height>320</height><insert_color_metadata>false</insert_color_metadata><respond_to_afd>None</respond_to_afd><sharpness>50</sharpness><stretch_to_output>false</stretch_to_output><timecode_passthrough>false</timecode_passthrough><vbi_passthrough>false</vbi_passthrough><width>480</width><h264_settings><adaptive_quantization>medium</adaptive_quantization><bitrate>5000000</bitrate><buf_fill_pct nil="true"/><buf_size nil="true"/><cabac>true</cabac><flicker_reduction>off</flicker_reduction><force_field_pictures>false</force_field_pictures><framerate_denominator nil="true"/><framerate_follow_source>true</framerate_follow_source><framerate_numerator nil="true"/><gop_b_reference>false</gop_b_reference><gop_closed_cadence>1</gop_closed_cadence><gop_markers>false</gop_markers><gop_num_b_frames>2</gop_num_b_frames><gop_size>90.0</gop_size><gop_size_units>frames</gop_size_units><interpolate_frc>false</interpolate_frc><look_ahead_rate_control>medium</look_ahead_rate_control><max_bitrate nil="true"/><max_qp nil="true"/><min_bitrate nil="true"/><min_buf_occ nil="true"/><min_i_interval>0</min_i_interval><min_qp nil="true"/><num_ref_frames>1</num_ref_frames><par_denominator nil="true"/><par_follow_source>true</par_follow_source><par_numerator nil="true"/><passes>1</passes><qp nil="true"/><repeat_pps>false</repeat_pps><rp2027_syntax>false</rp2027_syntax><scd>true</scd><sei_timecode>false</sei_timecode><slices>1</slices><slow_pal>false</slow_pal><softness nil="true"/><svq>0</svq><telecine>None</telecine><profile>Main</profile><rate_control_mode>CBR</rate_control_mode><gop_mode>fixed</gop_mode><interlace_mode>progressive</interlace_mode></h264_settings><selected_gpu nil="true"/><codec>h.264</codec></video_description><audio_description><audio_type>0</audio_type><follow_input_audio_type>true</follow_input_audio_type><follow_input_language_code>true</follow_input_language_code><language_code nil="true"/><order>1</order><stream_name nil="true"/><timecode_passthrough>false</timecode_passthrough><aac_settings><ad_broadcaster_mix>false</ad_broadcaster_mix><bitrate>96000</bitrate><coding_mode>2_0</coding_mode><latm_loas>false</latm_loas><mpeg2>false</mpeg2><sample_rate>48000</sample_rate><profile>LC</profile><rate_control_mode>CBR</rate_control_mode></aac_settings><codec>aac</codec></audio_description></stream_assembly><output_group><custom_name>udp_ts</custom_name><name nil="true"/><order>1</order><udp_group_settings><on_input_loss>drop_ts</on_input_loss><timed_metadata_id3_frame>PRIV</timed_metadata_id3_frame><timed_metadata_id3_period>10</timed_metadata_id3_period><name>udp_group_settings</name></udp_group_settings><type>udp_group_settings</type><output><arib_captions_passthrough>false</arib_captions_passthrough><description nil="true"/><ebif_passthrough>false</ebif_passthrough><extension>m2ts</extension><insert_amf_metadata>false</insert_amf_metadata><insert_private_metadata>false</insert_private_metadata><insert_scte35_esam>false</insert_scte35_esam><insert_timed_metadata>false</insert_timed_metadata><klv_passthrough>false</klv_passthrough><log_edit_points>false</log_edit_points><name_modifier nil="true"/><nielsen_id3_passthrough>false</nielsen_id3_passthrough><order>1</order><scte35_passthrough>false</scte35_passthrough><start_paused>false</start_paused><udp_settings><buffer_msec>1000</buffer_msec><max_ts_packet_count>7</max_ts_packet_count><mpts_membership>none</mpts_membership><destination><uri>udp://10.0.50.157:5901</uri></destination></udp_settings><m2ts_settings><arib>false</arib><audio_frames_per_pes>2</audio_frames_per_pes><bitrate>0</bitrate><drop_absent_streams>false</drop_absent_streams><dvb>false</dvb><es_rate>false</es_rate><null_packet_bitrate nil="true"/><pat_interval>100</pat_interval><pcr_every_pes>true</pcr_every_pes><pcr_period nil="true"/><pmt_interval>100</pmt_interval><program_num>1</program_num><scte35_pullup>0</scte35_pullup><segmentation_markers>none</segmentation_markers><segmentation_style>maintain_cadence</segmentation_style><segmentation_time nil="true"/><transport_stream_id nil="true"/><use_atsc_stream_type>false</use_atsc_stream_type><use_buffer_model>true</use_buffer_model><vbr>false</vbr><dvb_sdt_settings><output_sdt>sdt_follow</output_sdt><rep_interval>500</rep_interval><service_name/><service_provider_name/></dvb_sdt_settings><audio_pids>482-498</audio_pids><dvb_sub_pids>460-479</dvb_sub_pids><dvb_teletext_pid>499</dvb_teletext_pid><pmt_pid>480</pmt_pid><video_pid>481</video_pid></m2ts_settings><stream_assembly_name>stream_assembly_0</stream_assembly_name><container>m2ts</container></output></output_group></live_event>'))

    def test_getlastuuid_wrongdata(self):
        schedControl = SchedulerController()
        print(schedControl.getLastUUID(1))

    def test_getelapsed_wrongdata(self):
        schedControl = SchedulerController()
        print(schedControl.getElapsedInSeconds(1))

    def test_getduration_wrongdata(self):
        schedControl = SchedulerController()
        print(schedControl.getElapsedInSeconds(1))

    def test_getliveevent(self):
        schedControl = SchedulerController()
        print(schedControl.getLiveEvent())

    def test_updatelive(self):
        schedControl = SchedulerController()
        schedControl.updateLiveEvent(
            "<android.support.design.widget.AppBarLayout><android.support.v7.widget.Toolbar/></android.support.design.widget.AppBarLayout>")


if __name__ == '__main__':
    unittest.main()