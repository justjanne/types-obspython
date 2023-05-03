from typing import Optional, TypeVar, Generic, Callable

__T = TypeVar('T')


class WeakRef(Generic[__T]): ...


class Source: ...


class Scene: ...


class Data: ...


class View: ...


class SceneItem: ...


class Output: ...


class Encoder: ...


class EncoderPacket: ...


class Service: ...


class Settings: ...


class CallData: ...


class FrontendEvent: ...


class Profile: ...


class MediaFramesPerSecond: ...


class Property: ...


class Properties: ...


class FaderType:
    """
    One of the following values:
        OBS_FADER_CUBIC - A simple cubic fader for controlling audio levels
            This is a very common type of software fader since it yields good
            results while being quite performant.
            The input value is mapped to mul values with the simple formula x^3.
        OBS_FADER_IEC - A fader compliant to IEC 60-268-18
            This type of fader has several segments with different slopes that
            map deflection linearly to dB values. The segments are defined as
            in the following table::

                Deflection           | Volume
                ------------------------------------------
                [ 100   %, 75   % ]  | [   0 dB,   -9 dB ]
                [  75   %, 50   % ]  | [  -9 dB,  -20 dB ]
                [  50   %, 30   % ]  | [ -20 dB,  -30 dB ]
                [  30   %, 15   % ]  | [ -30 dB,  -40 dB ]
                [  15   %,  7.5 % ]  | [ -40 dB,  -50 dB ]
                [   7.5 %,  2.5 % ]  | [ -50 dB,  -60 dB ]
                [   2.5 %,  0   % ]  | [ -60 dB, -inf dB ]
        OBS_FADER_LOG - Logarithmic fader
    """


OBS_FADER_CUBIC: FaderType
OBS_FADER_IEC: FaderType
OBS_FADER_LOG: FaderType


class PeakMeterType:
    """
    One of the following values:
        SAMPLE_PEAK_METER - A simple peak meter measuring the maximum of all samples.
            This was a very common type of peak meter used for audio, but
            is not very accurate with regards to further audio processing.
        TRUE_PEAK_METER - An accurate peak meter measure the maximum of inter-samples.
            This meter is more computational intensive due to 4x oversampling
            to determine the true peak to an accuracy of +/- 0.5 dB.
    """


SAMPLE_PEAK_METER: PeakMeterType
TRUE_PEAK_METER: PeakMeterType


class EncoderType:
    """
    One of the following values:
        OBS_ENCODER_AUDIO - The encoder provides an audio codec
        OBS_ENCODER_VIDEO - The encoder provides a video codec
    """


OBS_ENCODER_AUDIO: EncoderType
OBS_ENCODER_VIDEO: EncoderType


class ScaleType:
    """
    One of the following values:
        OBS_SCALE_DISABLE
        OBS_SCALE_POINT
        OBS_SCALE_BICUBIC
        OBS_SCALE_BILINEAR
        OBS_SCALE_LANCZOS
        OBS_SCALE_AREA
    """


OBS_SCALE_DISABLE: ScaleType
OBS_SCALE_POINT: ScaleType
OBS_SCALE_BICUBIC: ScaleType
OBS_SCALE_BILINEAR: ScaleType
OBS_SCALE_LANCZOS: ScaleType
OBS_SCALE_AREA: ScaleType


class BlendingMethod:
    """
    One of the following values:
        OBS_BLEND_METHOD_DEFAULT
        OBS_BLEND_METHOD_SRGB_OFF
    """


OBS_BLEND_METHOD_DEFAULT: BlendingMethod
OBS_BLEND_METHOD_SRGB_OFF: BlendingMethod


class BlendingType:
    """
    One of the following values:
        OBS_BLEND_NORMAL
        OBS_BLEND_ADDITIVE
        OBS_BLEND_SUBTRACT
        OBS_BLEND_SCREEN
        OBS_BLEND_MULTIPLY
        OBS_BLEND_LIGHTEN
        OBS_BLEND_DARKEN
    """


OBS_BLEND_NORMAL: BlendingType
OBS_BLEND_ADDITIVE: BlendingType
OBS_BLEND_SUBTRACT: BlendingType
OBS_BLEND_SCREEN: BlendingType
OBS_BLEND_MULTIPLY: BlendingType
OBS_BLEND_LIGHTEN: BlendingType
OBS_BLEND_DARKEN: BlendingType


class ObjType:
    """
    One of the following values:
        OBS_OBJ_TYPE_INVALID
        OBS_OBJ_TYPE_SOURCE
        OBS_OBJ_TYPE_OUTPUT
        OBS_OBJ_TYPE_ENCODER
        OBS_OBJ_TYPE_SERVICE
    """


OBS_OBJ_TYPE_INVALID: ObjType
OBS_OBJ_TYPE_SOURCE: ObjType
OBS_OBJ_TYPE_OUTPUT: ObjType
OBS_OBJ_TYPE_ENCODER: ObjType
OBS_OBJ_TYPE_SERVICE: ObjType


class DeinterlaceMode:
    """
    One of the following values:
        OBS_DEINTERLACE_MODE_DISABLE
        OBS_DEINTERLACE_MODE_DISCARD
        OBS_DEINTERLACE_MODE_RETRO
        OBS_DEINTERLACE_MODE_RETRO
        OBS_DEINTERLACE_MODE_BLEND
        OBS_DEINTERLACE_MODE_BLEND_2X
        OBS_DEINTERLACE_MODE_LINEAR
        OBS_DEINTERLACE_MODE_LINEAR_2X
        OBS_DEINTERLACE_MODE_YADIF
        OBS_DEINTERLACE_MODE_YADIF_2X
    """


OBS_DEINTERLACE_MODE_DISABLE: DeinterlaceMode
OBS_DEINTERLACE_MODE_DISCARD: DeinterlaceMode
OBS_DEINTERLACE_MODE_RETRO: DeinterlaceMode
OBS_DEINTERLACE_MODE_RETRO: DeinterlaceMode
OBS_DEINTERLACE_MODE_BLEND: DeinterlaceMode
OBS_DEINTERLACE_MODE_BLEND_2X: DeinterlaceMode
OBS_DEINTERLACE_MODE_LINEAR: DeinterlaceMode
OBS_DEINTERLACE_MODE_LINEAR_2X: DeinterlaceMode
OBS_DEINTERLACE_MODE_YADIF: DeinterlaceMode
OBS_DEINTERLACE_MODE_YADIF_2X: DeinterlaceMode


class DeinterlaceFieldOrder:
    """
    One of the following values:
        OBS_DEINTERLACE_FIELD_ORDER_TOP
        OBS_DEINTERLACE_FIELD_ORDER_BOTTOM
    """


OBS_DEINTERLACE_FIELD_ORDER_TOP: DeinterlaceFieldOrder
OBS_DEINTERLACE_FIELD_ORDER_BOTTOM: DeinterlaceFieldOrder


class MonitoringType:
    """
    One of the following values:
        OBS_MONITORING_TYPE_NONE
        OBS_MONITORING_TYPE_MONITOR_ONLY
        OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT
    """


OBS_MONITORING_TYPE_NONE: MonitoringType
OBS_MONITORING_TYPE_MONITOR_ONLY: MonitoringType
OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT: MonitoringType


class TransitionTarget:
    """
    One of the following values:
        OBS_TRANSITION_SOURCE_A
        OBS_TRANSITION_SOURCE_B
    """


OBS_TRANSITION_SOURCE_A: TransitionTarget
OBS_TRANSITION_SOURCE_B: TransitionTarget


class TransitionMode:
    """
    One of the following values:
        OBS_TRANSITION_MODE_AUTO
        OBS_TRANSITION_MODE_MANUAL
    """


OBS_TRANSITION_MODE_AUTO: TransitionMode
OBS_TRANSITION_MODE_MANUAL: TransitionMode


class TransitionScaleType:
    """
    One of the following values:
        OBS_TRANSITION_SCALE_MAX_ONLY
        OBS_TRANSITION_SCALE_ASPECT
        OBS_TRANSITION_SCALE_STRETCH
    """


OBS_TRANSITION_SCALE_MAX_ONLY: TransitionScaleType
OBS_TRANSITION_SCALE_ASPECT: TransitionScaleType
OBS_TRANSITION_SCALE_STRETCH: TransitionScaleType


class SceneDuplicateType:
    """
    One of the following values:
        OBS_SCENE_DUP_REFS - Source refs only
        OBS_SCENE_DUP_COPY - Fully duplicate
        OBS_SCENE_DUP_PRIVATE_REFS - Source refs only (as private)
        OBS_SCENE_DUP_PRIVATE_COPY - Fully duplicate (as private)
    """


OBS_SCENE_DUP_REFS: SceneDuplicateType
OBS_SCENE_DUP_COPY: SceneDuplicateType
OBS_SCENE_DUP_PRIVATE_REFS: SceneDuplicateType
OBS_SCENE_DUP_PRIVATE_COPY: SceneDuplicateType


class SourceType:
    """
    One of the following values:
        OBS_SOURCE_TYPE_INPUT
        OBS_SOURCE_TYPE_FILTER
        OBS_SOURCE_TYPE_TRANSITION
        OBS_SOURCE_TYPE_SCENE
    """


OBS_SOURCE_TYPE_INPUT: SourceType
OBS_SOURCE_TYPE_FILTER: SourceType
OBS_SOURCE_TYPE_TRANSITION: SourceType
OBS_SOURCE_TYPE_SCENE: SourceType


class BalanceType:
    """
    One of the following values:
        OBS_BALANCE_TYPE_SINE_LAW
        OBS_BALANCE_TYPE_SQUARE_LAW
        OBS_BALANCE_TYPE_LINEAR
    """


OBS_BALANCE_TYPE_SINE_LAW: BalanceType
OBS_BALANCE_TYPE_SQUARE_LAW: BalanceType
OBS_BALANCE_TYPE_LINEAR: BalanceType


class MediaState:
    """
    One of the following values:
        OBS_MEDIA_STATE_NONE
        OBS_MEDIA_STATE_PLAYING
        OBS_MEDIA_STATE_OPENING
        OBS_MEDIA_STATE_BUFFERING
        OBS_MEDIA_STATE_PAUSED
        OBS_MEDIA_STATE_STOPPED
        OBS_MEDIA_STATE_ENDED
        OBS_MEDIA_STATE_ERROR
    """


OBS_MEDIA_STATE_NONE: MediaState
OBS_MEDIA_STATE_PLAYING: MediaState
OBS_MEDIA_STATE_OPENING: MediaState
OBS_MEDIA_STATE_BUFFERING: MediaState
OBS_MEDIA_STATE_PAUSED: MediaState
OBS_MEDIA_STATE_STOPPED: MediaState
OBS_MEDIA_STATE_ENDED: MediaState
OBS_MEDIA_STATE_ERROR: MediaState


class SpeakerLayout:
    """
    One of the following values:
        SPEAKERS_UNKNOWN - Unknown setting, fallback is stereo.
        SPEAKERS_MONO - Channels: MONO
        SPEAKERS_STEREO - Channels: FL, FR
        SPEAKERS_2POINT1 - Channels: FL, FR, LFE
        SPEAKERS_4POINT0 - Channels: FL, FR, FC, RC
        SPEAKERS_4POINT1 - Channels: FL, FR, FC, LFE, RC
        SPEAKERS_5POINT1 - Channels: FL, FR, FC, LFE, RL, RR
        SPEAKERS_7POINT1 - Channels: FL, FR, FC, LFE, RL, RR, SL, SR
    """


SPEAKERS_UNKNOWN: SpeakerLayout
SPEAKERS_MONO: SpeakerLayout
SPEAKERS_STEREO: SpeakerLayout
SPEAKERS_2POINT1: SpeakerLayout
SPEAKERS_4POINT0: SpeakerLayout
SPEAKERS_4POINT1: SpeakerLayout
SPEAKERS_5POINT1: SpeakerLayout
SPEAKERS_7POINT1: SpeakerLayout


class VideoFormat:
    """
    One of the following values:
        VIDEO_FORMAT_NONE
    planar 4:2:0 formats
        VIDEO_FORMAT_I420 - three-plane
        VIDEO_FORMAT_NV12 - two-plane, luma and packed chroma
    packed 4:2:2 formats
        VIDEO_FORMAT_YVYU
        VIDEO_FORMAT_YUY2 - YUYV
        VIDEO_FORMAT_UYVY
    packed uncompressed formats
        VIDEO_FORMAT_RGBA
        VIDEO_FORMAT_BGRA
        VIDEO_FORMAT_BGRX
        VIDEO_FORMAT_Y800 - grayscale
    planar 4:4:4
        VIDEO_FORMAT_I444
    more packed uncompressed formats
        VIDEO_FORMAT_BGR3
        VIDEO_FORMAT_I422 - planar 4:2:2
        VIDEO_FORMAT_I40A - planar 4:2:0 with alpha
        VIDEO_FORMAT_I42A - planar 4:2:2 with alpha
        VIDEO_FORMAT_YUVA - planar 4:4:4 with alpha
        VIDEO_FORMAT_AYUV - packed 4:4:4 with alpha
    planar 4:2:0 format, 10 bpp
        VIDEO_FORMAT_I010 - three-plane
        VIDEO_FORMAT_P010 - two-plane, luma and packed chroma
    planar 4:2:2 10 bits
        VIDEO_FORMAT_I210 - Little Endian
    planar 4:4:4 12 bits
        VIDEO_FORMAT_I412 - Little Endian
    planar 4:4:4 12 bits with alpha
        VIDEO_FORMAT_YA2L - Little Endian
    """


VIDEO_FORMAT_NONE: VideoFormat
VIDEO_FORMAT_I420: VideoFormat
VIDEO_FORMAT_NV12: VideoFormat
VIDEO_FORMAT_YVYU: VideoFormat
VIDEO_FORMAT_YUY2: VideoFormat
VIDEO_FORMAT_UYVY: VideoFormat
VIDEO_FORMAT_RGBA: VideoFormat
VIDEO_FORMAT_BGRA: VideoFormat
VIDEO_FORMAT_BGRX: VideoFormat
VIDEO_FORMAT_Y800: VideoFormat
VIDEO_FORMAT_I444: VideoFormat
VIDEO_FORMAT_BGR3: VideoFormat
VIDEO_FORMAT_I422: VideoFormat
VIDEO_FORMAT_I40A: VideoFormat
VIDEO_FORMAT_I42A: VideoFormat
VIDEO_FORMAT_YUVA: VideoFormat
VIDEO_FORMAT_AYUV: VideoFormat
VIDEO_FORMAT_I010: VideoFormat
VIDEO_FORMAT_P010: VideoFormat
VIDEO_FORMAT_I210: VideoFormat
VIDEO_FORMAT_I412: VideoFormat
VIDEO_FORMAT_YA2L: VideoFormat


class PropertyType:
    """
    One of the following values:
        OBS_PROPERTY_INVALID
        OBS_PROPERTY_BOOL
        OBS_PROPERTY_INT
        OBS_PROPERTY_FLOAT
        OBS_PROPERTY_TEXT
        OBS_PROPERTY_PATH
        OBS_PROPERTY_LIST
        OBS_PROPERTY_COLOR
        OBS_PROPERTY_BUTTON
        OBS_PROPERTY_FONT
        OBS_PROPERTY_EDITABLE_LIST
        OBS_PROPERTY_FRAME_RATE
        OBS_PROPERTY_GROUP
    """


OBS_PROPERTY_INVALID: PropertyType
OBS_PROPERTY_BOOL: PropertyType
OBS_PROPERTY_INT: PropertyType
OBS_PROPERTY_FLOAT: PropertyType
OBS_PROPERTY_TEXT: PropertyType
OBS_PROPERTY_PATH: PropertyType
OBS_PROPERTY_LIST: PropertyType
OBS_PROPERTY_COLOR: PropertyType
OBS_PROPERTY_BUTTON: PropertyType
OBS_PROPERTY_FONT: PropertyType
OBS_PROPERTY_EDITABLE_LIST: PropertyType
OBS_PROPERTY_FRAME_RATE: PropertyType
OBS_PROPERTY_GROUP: PropertyType
OBS_PROPERTY_COLOR_ALPHA: PropertyType


class ComboFormat:
    """
    Can be one of the following values:
        OBS_COMBO_FORMAT_INT - Integer list
        OBS_COMBO_FORMAT_FLOAT - Floating point list
        OBS_COMBO_FORMAT_STRING - String list
    """


OBS_COMBO_FORMAT_INT: ComboFormat
OBS_COMBO_FORMAT_FLOAT: ComboFormat
OBS_COMBO_FORMAT_STRING: ComboFormat


class ComboType:
    """
    Can be one of the following values:
        OBS_COMBO_TYPE_EDITABLE - Can be edited. Only used with string lists.
        OBS_COMBO_TYPE_LIST - Not editable.
    """


OBS_COMBO_TYPE_EDITABLE: ComboType
OBS_COMBO_TYPE_LIST: ComboType


class EditableListType:
    """
    Can be one of the following values:
        OBS_EDITABLE_LIST_TYPE_STRINGS - An editable list of strings.
        OBS_EDITABLE_LIST_TYPE_FILES - An editable list of files.
        OBS_EDITABLE_LIST_TYPE_FILES_AND_URLS - An editable list of files and URLs.
    """


OBS_EDITABLE_LIST_TYPE_STRINGS: EditableListType
OBS_EDITABLE_LIST_TYPE_FILES: EditableListType
OBS_EDITABLE_LIST_TYPE_FILES_AND_URLS: EditableListType


class PathType:
    """
    Can be one of the following values:
        OBS_PATH_FILE - File (for reading)
        OBS_PATH_FILE_SAVE - File (for writing)
        OBS_PATH_DIRECTORY - Directory
    """


OBS_PATH_FILE: PathType
OBS_PATH_FILE_SAVE: PathType
OBS_PATH_DIRECTORY: PathType


class TextType:
    """
    Can be one of the following values:
        OBS_TEXT_DEFAULT - Single line of text
        OBS_TEXT_PASSWORD - Single line of text (passworded)
        OBS_TEXT_MULTILINE - Multi-line text
        OBS_TEXT_INFO - Read-only informative text, behaves differently depending on wether description, string value and long description are set
    """


OBS_TEXT_DEFAULT: TextType
OBS_TEXT_PASSWORD: TextType
OBS_TEXT_MULTILINE: TextType
OBS_TEXT_INFO: TextType


class TextInfoType:
    """
    One of the following values:
        OBS_TEXT_INFO_NORMAL
        OBS_TEXT_INFO_WARNING
        OBS_TEXT_INFO_ERROR
    """


OBS_TEXT_INFO_NORMAL: TextInfoType
OBS_TEXT_INFO_WARNING: TextInfoType
OBS_TEXT_INFO_ERROR: TextInfoType


class NumberType: ...


OBS_NUMBER_SCROLLER: NumberType
OBS_NUMBER_SLIDER: NumberType


class GroupType:
    """
    Can be one of the following values:
        OBS_GROUP_NORMAL - A normal group with just a name and content.
        OBS_GROUP_CHECKABLE - A checkable group with a checkbox, name and content.
    """
    pass


OBS_GROUP_NORMAL: GroupType
OBS_GROUP_CHECKABLE: GroupType


class ButtonType:
    """
    One of the following values:
        OBS_BUTTON_DEFAULT
        OBS_BUTTON_URL
    """


OBS_BUTTON_DEFAULT: ButtonType
OBS_BUTTON_URL: ButtonType


def obs_get_version() -> int:
    """The current core version"""


def obs_get_version_string() -> str:
    """The current core version string"""


def obs_set_locale(locale: str) -> None:
    """Sets a new locale to use for modules.
    This will call obs_module_set_locale for each module with the new locale.
    :param locale: The locale to use for modules
    """


def obs_get_locale() -> str:
    """The current locale"""


# obs_reset_video
# obs_reset_audio
# obs_reset_audio2
# obs_get_video_info
# obs_get_video_sdr_white_level
# obs_get_video_hdr_nominal_peak_level
# obs_set_video_sdr_white_level
# obs_get_audio_info

def obs_enum_source_types() -> list[str]:
    """
    Enumerates all source types (inputs, filters, transitions, etc).
    """


def obs_enum_input_types() -> list[str]:
    """
    Enumerates all available input source types.
    Inputs are general source inputs (such as capture sources, device sources, etc).
    """


def obs_enum_filter_types() -> list[str]:
    """
    Enumerates all available filter source types.
    Filters are sources that are used to modify the video/audio output of other sources.
    """


def obs_enum_transition_types() -> list[str]:
    """
    Enumerates all available transition source types.
    Transitions are sources used to transition between two or more other sources.
    """


def obs_enum_output_types() -> list[str]:
    """
    Enumerates all available output types.
    """


def obs_enum_encoder_types() -> list[str]:
    """
    Enumerates all available encoder types.
    """


def obs_enum_service_types() -> list[str]:
    """
    Enumerates all available service types.
    """


def obs_get_source_by_name(name: str) -> Optional[Source]:
    """
    Gets a source by its name.

    Increments the source reference counter, use obs_source_release() to release it when complete.
    :param name: Name of the source
    """


def obs_get_transition_by_name(name: str) -> Optional[Source]:
    """
    Gets a transition by its name.

    Increments the source reference counter, use obs_source_release() to release it when complete.
    :param name: Name of the transition
    """


def obs_get_scene_by_name(name: str) -> Optional[Source]:
    """
    Gets a scene by its name.

    Increments the source reference counter, use obs_source_release() to release it when complete.
    :param name: Name of the scene
    """


def obs_get_output_by_name(name: str) -> Optional[Source]:
    """
    Gets a output by its name.

    Increments the source reference counter, use obs_source_release() to release it when complete.
    :param name: Name of the output
    """


def obs_get_encoder_by_name(name: str) -> Optional[Source]:
    """
    Gets a encoder by its name.

    Increments the source reference counter, use obs_source_release() to release it when complete.
    :param name: Name of the encoder
    """


def obs_get_service_by_name(name: str) -> Optional[Source]:
    """
    Gets a service by its name.

    Increments the source reference counter, use obs_source_release() to release it when complete.
    :param name: Name of the service
    """


def obs_save_source(source: Source) -> Data:
    """
    :return: A new reference to a source’s saved data.
             Use obs_data_release() to release it when complete.
    """


def obs_load_source(data: Data) -> Source:
    """
    :return: Loads a source from settings data
    """


def obs_load_private_source(data: Data) -> Source:
    """
    :return: Loads a private source from settings data
    """


def obs_set_output_source(channel: int, source: Source) -> None:
    """
    Sets the primary output source for a channel.
    """


def obs_get_output_source(channel: int) -> Source:
    """
    Gets the primary output source for a channel and increments the reference counter for that source.
    Use obs_source_release() to release.
    """


def obs_audio_monitoring_available() -> bool:
    """
    :return: Whether audio monitoring is supported and available on the current platform
    """


def obs_get_video_frame_time() -> int:
    """
    :return: Timestamp of the current frame in nanoseconds
    """


def obs_get_active_fps() -> float:
    """
    :return: The current FPS average
    """


def obs_get_average_frame_time_ns() -> int:
    """
    :return: Average time spent per frame in nanoseconds
    """


def obs_get_frame_interval_ns() -> int:
    """
    :return: Time delta in nanoseconds since the last frame
    """


def obs_get_total_frames() -> int:
    """
    :return: Number of total frames
    """


def obs_get_lagged_frames() -> int:
    """
    :return: Number of dropped frames
    """


def obs_apply_private_data(settings: Data): ...


def obs_set_private_data(settings: Data): ...


def obs_get_private_data() -> Data: ...


# View context

def obs_view_create() -> View:
    """
    Creates a view context.

    A view can be used for things like separate previews, or drawing sources separately.
    """


def obs_view_destroy(view: View):
    """
    Destroys this view context
    """


def obs_view_set_source(view: View, channel: int, source: Source):
    """
    Sets the source to be used for this view context.
    """


def obs_view_get_source(view: View, channel: int):
    """
    Gets the source currently in use for this view context
    """


def obs_view_render(view: View):
    """
    Renders the sources of this view context
    """


def obs_view_add(view: View):
    """
    Adds a view to the main render loop, with current obs_get_video_info state
    """


# def obs_view_add2(view: View, ovi: ObsVideoInfo):

def obs_view_remove(view: View):
    """
    Removes a view from the main render loop
    """


# Display context

# TODO?

# Sources

def obs_source_get_display_name(id: str) -> str:
    """
    Returns the translated display name of a source
    """


def obs_source_create(id: str, name: str, settings: Data, hotkeys: Data) -> Source:
    """
    Creates a source of the specified type with the specified settings.

    The "source" context is used for anything related to presenting or modifying video/audio.
    Use obs_source_release to release it.
    """


def obs_source_create_private(id: str, name: str, settings: Data) -> Source: ...


def obs_source_duplicate(source: Source, desired_name: str, create_private: bool) -> Source:
    """
    if source has OBS_SOURCE_DO_NOT_DUPLICATE output flag set, only returns a reference
    """


def obs_source_release(source: Source) -> None: ...


def obs_weak_source_addref(weak: WeakRef[Source]) -> None: ...


def obs_weak_source_release(weak: WeakRef[Source]) -> None: ...


def obs_source_get_ref(source: Source) -> Source: ...


def obs_source_get_weak_source(source: Source) -> WeakRef[Source]: ...


def obs_weak_source_get_source(weak: WeakRef[Source]) -> Source: ...


def obs_weak_source_expired(weak: WeakRef[Source]) -> bool: ...


def obs_weak_source_references_source(weak: WeakRef[Source], source: Source) -> bool: ...


def obs_source_remove(source: Source):
    """
    Notifies all references that the source should be released
    """


def obs_source_removed(source: Source) -> bool:
    """
    Returns true if the source should be released
    """


def obs_source_set_hidden(source: Source, hidden: bool) -> None:
    """
    The 'hidden' flag is not the same as a sceneitem's visibility. It is a property that determines if it can be
    found through searches.

    Simply sets a 'hidden' flag when the source is still alive but shouldn't be found
    """


def obs_source_is_hidden(source: Source) -> bool:
    """
    Returns the current 'hidden' state on the source
    """


def obs_source_get_output_flags(source: Source) -> int:
    """
    Returns capability flags of a source
    """


def obs_get_source_output_flags(id: str) -> int:
    """
    Returns capability flags of a source type
    """


def obs_get_source_defaults(id: str) -> Data:
    """
    Gets the default settings for a source type
    """


def obs_get_source_properties(id: str) -> Properties:
    """
    Returns the property list, if any. Free with obs_properties_destroy
    """


# def obs_source_get_missing_files
# def obs_source_replace_missing_files

def obs_is_source_configurable(id: str) -> bool:
    """
    Returns whether the source has custom properties or not
    """


def obs_source_configurable(source: Source) -> bool: ...


def obs_source_properties(source: Source) -> Properties:
    """
    Returns the properties list for a specific existing source. Free with obs_properties_destroy
    """


def obs_source_update(source: Source, settings: Data) -> None:
    """
    Updates settings for this source
    """


def obs_source_reset_settings(source: Source, settings: Data) -> None: ...


def obs_source_video_render(source: Source) -> None:
    """
    Renders a video source.
    """


def obs_source_get_width(source: Source) -> int:
    """
    Gets the width of a source (if it has video)
    """


def obs_source_get_height(source: Source) -> int:
    """
    Gets the height of a source (if it has video)
    """


# def obs_source_get_color_space
# def obs_source_get_texcoords_centered

def obs_filter_get_target(filter: Source) -> Optional[Source]:
    """
    If the source is a filter, returns the target source of the filter. Only guaranteed to be valid inside the
    video_render, filter_audio, filter_video, and filter_remove callbacks.
    """


def obs_source_default_render(source: Source) -> None:
    """
    Used to directly render a non-async source without any filter processing
    """


def obs_source_filter_add(source: Source, filter: Source) -> None:
    """
    Adds a filter to the source (which is used whenever the source is used)
    """


def obs_source_filter_remove(source: Source, filter: Source) -> None:
    """
    Removes a filter from the source
    """


# def obs_source_filter_set_order

def obs_source_get_settings(source: Source) -> Data:
    """
    Gets the settings string for a source
    """


def obs_source_get_name(source: Source) -> str:
    """
    Gets the name of a source
    """


def obs_source_set_name(source: Source, name: str) -> None:
    """
    Sets the name of a source
    """


def obs_source_get_type(source: Source) -> SourceType:
    """
    Gets the source type
    """


def obs_source_get_id(source: Source) -> str:
    """
    Gets the source identifier
    """


def obs_source_get_unversioned_id(source: Source) -> str: ...


def obs_source_set_volume(source: Source, volume: float) -> None:
    """
    Sets the user volume for a source that has audio output
    """


def obs_source_get_volume(source: Source) -> float:
    """
    Gets the user volume for a source that has audio output
    """


def obs_source_get_speaker_layout(source: Source) -> SpeakerLayout:
    """
    Gets speaker layout of a source
    """


def obs_source_set_balance_value(source: Source, balance: float) -> None:
    """
    Sets the balance value for a stereo audio source
    """


def obs_source_get_balance_value(source: Source) -> float:
    """
    Gets the balance value for a stereo audio source
    """


def obs_source_set_sync_offset(source: Source, offset: int) -> None:
    """
    Sets the audio sync offset (in nanoseconds) for a source
    """


def obs_source_get_sync_offset(source: Source) -> int:
    """
    Gets the audio sync offset (in nanoseconds) for a source
    """


def obs_source_active(source: Source) -> bool:
    """
    Returns true if active, false if not
    """


def obs_source_showing(source: Source) -> bool:
    """
    Returns true if currently displayed somewhere (active or not), false if not
    """


def obs_source_set_flags(source: Source, flags: int) -> None:
    """
    Sets source flags.  Note that these are different from the main output flags. These are generally things that
    can be set by the source or user, while the output flags are more used to determine capabilities of a source.
    """


def obs_source_get_flags(source: Source) -> int:
    """
    Gets source flags.
    """


def obs_source_set_audio_mixers(mixers: int) -> None:
    """
    Sets audio mixer flags. These flags are used to specify which mixers the source's audio should be applied to.
    """


def obs_source_get_audio_mixers(source: Source) -> int:
    """
    Gets audio mixer flags
    """


def obs_source_inc_showing(source: Source) -> None:
    """
    Increments the 'showing' reference counter to indicate that the source is being shown somewhere.
    If the reference counter was 0, will call the 'show' callback.
    """


def obs_source_inc_active(source: Source) -> None:
    """
    Increments the 'active' reference counter to indicate that the source is fully active. If the reference counter
    was 0, will call the 'activate' callback.

    Unlike obs_source_inc_showing, this will cause children of this source to be considered showing as well
    (currently used by transition previews to make the stinger transition show correctly).  obs_source_inc_showing
    should generally be used instead.
    """


def obs_source_dec_showing(source: Source) -> None: ...


def obs_source_dec_active(source: Source) -> None: ...


# obs_source_enum_filters

def obs_source_get_filter_by_name(source: Source, name: str) -> Optional[Source]:
    """
    Gets a filter of a source by its display name.
    """


def obs_source_filter_count(source: Source) -> int:
    """
    Gets the number of filters the source has.
    """


def obs_source_copy_filters(dst: Source, src: Source) -> None: ...


def obs_source_copy_single_filter(dst: Source, filter: Source) -> None: ...


def obs_source_enabled(source: Source) -> bool: ...


def obs_source_set_enabled(source: Source, enabled: bool) -> None: ...


def obs_source_muted(source: Source) -> bool: ...


def obs_source_set_muted(source: Source, muted: bool) -> None: ...


def obs_source_push_to_mute_enabled(source: Source) -> bool: ...


def obs_source_enable_push_to_mute(source: Source, enabled: bool) -> None: ...


def obs_source_get_push_to_mute_delay(source: Source) -> int: ...


def obs_source_set_push_to_mute_delay(source: Source, delay: int) -> None: ...


def obs_source_push_to_talk_enabled(source: Source) -> bool: ...


def obs_source_enable_push_to_talk(source: Source, enabled: bool) -> None: ...


def obs_source_get_push_to_talk_delay(source: Source) -> int: ...


def obs_source_set_push_to_talk_delay(source: Source, delay: int) -> None: ...


def obs_source_set_deinterlace_mode(source: Source, mode: DeinterlaceMode) -> None: ...


def obs_source_get_deinterlace_mode(source: Source) -> DeinterlaceMode: ...


def obs_source_set_deinterlace_field_order(source: Source, field_order: DeinterlaceFieldOrder) -> None: ...


def obs_source_get_deinterlace_field_order(source: Source) -> DeinterlaceFieldOrder: ...


def obs_source_set_monitoring_type(source: Source, type: MonitoringType) -> None: ...


def obs_source_get_monitoring_type(source: Source) -> MonitoringType: ...


def obs_source_get_private_settings(item: Source) -> Data:
    """
    Gets private front-end settings data. This data is saved/loaded automatically.
    Returns an incremented reference.
    """


# def obs_source_backup_filters
# def obs_source_restore_filters

# Media controls
def obs_source_media_play_pause(source: Source, pause: bool) -> None: ...


def obs_source_media_restart(source: Source) -> None: ...


def obs_source_media_stop(source: Source) -> None: ...


def obs_source_media_next(source: Source) -> None: ...


def obs_source_media_previous(source: Source) -> None: ...


def obs_source_media_get_duration(source: Source) -> int: ...


def obs_source_media_get_time(source: Source) -> int: ...


def obs_source_media_set_time(source: Source, ms: int) -> None: ...


def obs_source_media_get_state(source: Source) -> MediaState: ...


def obs_source_media_started(source: Source) -> None: ...


def obs_source_media_ended(source: Source) -> None: ...


# Transition-specific functions

def obs_transition_get_source(transition: Source, target: TransitionTarget) -> Source: ...


def obs_transition_clear(transition: Source) -> None: ...


def obs_transition_get_active_source(transition: Source) -> Source: ...


def obs_transition_start(transition: Source, mode: TransitionMode, duration_ms: int,
                         dest: Source) -> bool: ...


def obs_transition_set(transition: Source, source: Source) -> None: ...


def obs_transition_set_manual_time(transition: Source, t: float) -> None: ...


def obs_transition_set_manual_torque(transition: Source, torque: float, clamp: float) -> None: ...


def obs_transition_set_scale_type(transition: Source, type: TransitionScaleType) -> None: ...


def obs_transition_get_scale_type(transition: Source) -> TransitionScaleType: ...


def obs_transition_set_alignment(transition: Source, alignment: int) -> None: ...


def obs_transition_get_alignment(transition: Source) -> int: ...


def obs_transition_set_size(cx: int, cy: int) -> None: ...


# def obs_transition_get_size

# Scenes

def obs_scene_create(name: str) -> Scene: ...


def obs_scene_create_private(name: str) -> Scene: ...


def obs_scene_duplicate(scene: Scene, name: str, type: SceneDuplicateType) -> Scene:
    """
    Duplicates a scene.
    """


def obs_scene_release(scene: Scene) -> None: ...


def obs_scene_get_ref(scene: Scene) -> Scene: ...


def obs_scene_get_source(scene: Scene) -> Source:
    """
    Gets the scene's source context
    """


def obs_scene_from_source(source: Source) -> Optional[Scene]:
    """
    Gets the scene from its source, or None if not a scene
    """


def obs_scene_find_source(scene: Scene, name: str) -> Optional[SceneItem]:
    """
    Determines whether a source is within a scene
    """


def obs_scene_find_source_recursive(scene: Scene, name: str) -> Optional[SceneItem]: ...


def obs_scene_find_sceneitem_by_id(scene: Scene, id: int) -> Optional[SceneItem]: ...


def obs_source_is_scene(source: Source) -> bool: ...


def obs_scene_add(scene: Scene, source: Source) -> SceneItem:
    """
    Adds/creates a new scene item for a source
    """


def obs_sceneitem_addref(item: SceneItem) -> None: ...


def obs_sceneitem_release(item: SceneItem) -> None: ...


def obs_sceneitem_remove(item: SceneItem) -> None:
    """
    Removes a scene item.
    """


# def obs_sceneitems_add
# def obs_sceneitem_save

def obs_sceneitem_set_id(sceneitem: SceneItem, id: int) -> None:
    """
    Set the ID of a sceneitem
    """


def obs_scene_sceneitem_from_source(scene: Scene, source: Source) -> Optional[SceneItem]:
    """
    Tries to find the sceneitem of the source in a given scene. Returns None if not found
    """


def obs_scene_save_transform_states(scene: Scene, all_items: bool) -> Data:
    """
    Save all the transform states for a current scene's sceneitems
    """


def obs_scene_load_transform_states(state: Data) -> None:
    """
    Load all the transform states of sceneitems in that scene
    """


def obs_sceneitem_get_order_position(item: SceneItem) -> int:
    """
    Gets a sceneitem's order in its scene
    """


def obs_sceneitem_get_scene(item: SceneItem) -> Scene:
    """
    Gets the scene parent associated with the scene item.
    """


def obs_sceneitem_get_source(item: SceneItem) -> Source:
    """
    Gets the source of a scene item.
    """


def obs_sceneitem_select(item: SceneItem, select: bool) -> None: ...


def obs_sceneitem_selected(item: SceneItem) -> bool: ...


def obs_sceneitem_locked(item: SceneItem) -> bool: ...


def obs_sceneitem_set_locked(item: SceneItem, lock: bool) -> None: ...


# def obs_sceneitem_set_pos
# def obs_sceneitem_set_rot
# def obs_sceneitem_set_scale
# def obs_sceneitem_set_alignment
# def obs_sceneitem_set_order
# def obs_sceneitem_set_order_position
# def obs_sceneitem_set_bounds_type
# def obs_sceneitem_set_bounds_alignment
# def obs_sceneitem_set_bounds

def obs_sceneitem_get_id(item: SceneItem) -> int: ...


# def obs_sceneitem_get_pos
# def obs_sceneitem_get_rot
# def obs_sceneitem_get_scale
# def obs_sceneitem_get_alignment
# def obs_sceneitem_get_bounds_type
# def obs_sceneitem_get_bounds_alignment
# def obs_sceneitem_get_bounds
# def obs_sceneitem_get_info
# def obs_sceneitem_set_info
# def obs_sceneitem_get_draw_transform
# def obs_sceneitem_get_box_transform
# def obs_sceneitem_get_box_scale

def obs_sceneitem_visible(item: SceneItem) -> bool: ...


def obs_sceneitem_set_visible(item: SceneItem, visible: bool) -> None: ...


# def obs_sceneitem_set_crop
# def obs_sceneitem_get_crop

def obs_sceneitem_set_scale_filter(item: SceneItem, filter: ScaleType) -> None: ...


def obs_sceneitem_get_scale_filter(item: SceneItem) -> ScaleType: ...


def obs_sceneitem_set_blending_method(item: SceneItem, method: BlendingMethod) -> None: ...


def obs_sceneitem_get_blending_method(item: SceneItem) -> BlendingMethod: ...


def obs_sceneitem_set_blending_mode(item: SceneItem, mode: BlendingType) -> None: ...


def obs_sceneitem_get_blending_mode(item: SceneItem) -> BlendingType: ...


def obs_sceneitem_force_update_transform(item: SceneItem) -> None: ...


def obs_sceneitem_defer_update_begin(item: SceneItem) -> None: ...


def obs_sceneitem_defer_update_end(item: SceneItem) -> None: ...


def obs_sceneitem_get_private_settings(item: SceneItem) -> Data:
    """
    Gets private front-end settings data. This data is saved/loaded automatically. Returns an incremented reference.
    """


def obs_scene_add_group(scene: Scene, name: str) -> SceneItem: ...


# def obs_scene_insert_group
# def obs_scene_add_group2
# def obs_scene_insert_group2

def obs_scene_get_group(scene: Scene, name: str) -> SceneItem: ...


def obs_sceneitem_is_group(item: SceneItem) -> bool: ...


def obs_sceneitem_group_get_scene(group: SceneItem) -> Scene: ...


def obs_sceneitem_group_ungroup(group: SceneItem) -> None: ...


# def obs_sceneitem_group_ungroup2

def obs_sceneitem_group_add_item(group: SceneItem, item: SceneItem) -> None: ...


def obs_sceneitem_group_remove_item(group: SceneItem, item: SceneItem) -> None: ...


def obs_sceneitem_get_group(scene: Scene, item: SceneItem) -> Optional[SceneItem]: ...


def obs_source_is_group(source: Source) -> bool: ...


def obs_scene_is_group(scene: Scene) -> bool: ...


# def obs_sceneitem_group_enum_items

def obs_group_from_source(source: Source) -> Optional[Scene]:
    """
    Gets the group from its source, or NULL if not a group
    """


def obs_group_or_scene_from_source(source: Source) -> Scene: ...


def obs_sceneitem_defer_group_resize_begin(item: SceneItem) -> None: ...


def obs_sceneitem_defer_group_resize_end(item: SceneItem) -> None: ...


def obs_sceneitem_set_show_transition(item: SceneItem, transition: Source) -> None: ...


def obs_sceneitem_set_show_transition_duration(item: SceneItem, duration_ms: int) -> None: ...


def obs_sceneitem_set_transition(item: SceneItem, show: bool, transition: Source) -> None: ...


def obs_sceneitem_get_transition(item: SceneItem, show: bool, duration_ms: int) -> None: ...


def obs_sceneitem_get_transition_duration(item: SceneItem, show: bool) -> int: ...


def obs_sceneitem_do_transition(item: SceneItem, visible: bool) -> None: ...


def obs_sceneitem_transition_load(item: SceneItem, data: Data, show: bool) -> None: ...


def obs_sceneitem_transition_save(item: SceneItem, show: bool) -> Data: ...


def obs_scene_prune_sources(scene: Scene) -> None: ...


# Outputs

def obs_output_get_display_name(id: str) -> str: ...


def obs_output_create(id: str, name: str, settings: Data, hotkeys: Data):
    """
    Creates an output.

    Outputs allow outputting to file, outputting to network, outputting to directshow, or other custom outputs.
    """


def obs_output_release(output: Output) -> None: ...


def obs_weak_output_addref(weak: WeakRef[Output]) -> None: ...


def obs_weak_output_release(weak: WeakRef[Output]) -> None: ...


def obs_output_get_ref(output: Output) -> Output: ...


def obs_output_get_weak_output(output: Output) -> WeakRef[Output]: ...


def obs_weak_output_get_output(output: WeakRef[Output]) -> Output: ...


def obs_weak_output_references_output(weak: WeakRef[Output], output: Output) -> bool: ...


def obs_output_get_name(output: Output) -> str: ...


def obs_output_start(output: Output) -> bool:
    """
    Starts the output.
    """


def obs_output_stop(output: Output) -> None:
    """
    Stops the output.
    """


# On reconnection, start where it left of on reconnection.  Note however that
# this option will consume extra memory to continually increase delay while
# waiting to reconnect.
OBS_OUTPUT_DELAY_PRESERVE: int


def obs_output_set_delay(output: Output, delay_sec: int, flags: int) -> None:
    """
    Sets the current output delay, in seconds (if the output supports delay).

    If delay is currently active, it will set the delay value, but will not affect the current delay, it will only
    affect the next time the output is activated.
    """


def obs_output_get_delay(output: Output) -> int:
    """
    Gets the currently set delay value, in seconds.
    """


def obs_output_get_active_delay(output: Output) -> int:
    """
    If delay is active, gets the currently active delay value, in seconds.
    """


def obs_output_force_stop(output: Output) -> None:
    """
    Forces the output to stop.  Usually only used with delay.
    """


def obs_output_active(output: Output) -> bool:
    """
    Returns whether the output is active
    """


def obs_output_get_flags(output: Output) -> int:
    """
    Returns output capability flags
    """


def obs_get_output_flags(id: str) -> int:
    """
    Returns output capability flags
    """


def obs_output_defaults(id: str) -> Data:
    """
    Gets the default settings for an output type
    """


def obs_get_output_properties(id: str) -> Properties:
    """
    Returns the property list, if any. Free with obs_properties_destroy
    """


def obs_output_properties(output: Output) -> Properties:
    """
    Returns the property list of an existing output, if any. Free with obs_properties_destroy
    """


def obs_output_update(output: Output, settings: Data) -> None:
    """
    Updates the settings for this output context
    """


def obs_output_can_pause(output: Output) -> bool:
    """
    Specifies whether the output can be paused
    """


def obs_output_pause(output: Output, pause: bool) -> bool:
    """
    Pauses the output (if the functionality is allowed by the output
    """


def obs_output_paused(output: Output) -> bool:
    """
    Returns whether output is paused
    """


def obs_output_get_settings(output: Output) -> Data:
    """
    Gets the current output settings string
    """


# def obs_output_set_media
# def obs_output_video
# def obs_output_audio

def obs_output_set_mixer(output: Output, mixer_idx: int) -> None:
    """
    Sets the current audio mixer for non-encoded outputs
    """


def obs_output_get_mixer(output: Output) -> int:
    """
    Gets the current audio mixer for non-encoded outputs
    """


def obs_output_set_mixers(output: Output, mixers: int) -> None:
    """
    Sets the current audio mixes (mask) for a non-encoded multi-track output
    """


def obs_output_get_mixers(output: Output) -> int:
    """
    Gets the current audio mixes (mask) for a non-encoded multi-track output
    """


def obs_output_set_video_encoder(output: Output, encoder: Encoder) -> None:
    """
    Sets the current video encoder associated with this output, required for encoded outputs
    """


def obs_output_set_audio_encoder(output: Output, idx: int) -> None:
    """
    Sets the current audio encoder associated with this output, required for encoded outputs.

    The idx parameter specifies the audio encoder index to set the encoder to.
    Only used with outputs that have multiple audio outputs (RTMP typically), otherwise the parameter is ignored.
    """


def obs_output_get_video_encoder(output: Output) -> Encoder:
    """
    Returns the current video encoder associated with this output
    """


def obs_output_get_audio_encoder(output: Output, idx: int) -> Encoder:
    """
    Returns the current audio encoder associated with this output

    The idx parameter specifies the audio encoder index.  Only used with outputs that have multiple audio outputs,
    otherwise the parameter is ignored.
    """


def obs_output_set_service(output: Output, service: Service):
    """
    Sets the current service associated with this output.
    """


def obs_output_get_service(output: Output) -> Service:
    """
    Gets the current service associated with this output.
    """


def obs_output_set_reconnect_settings(output: Output, retry_count: int, retry_sec: int) -> None:
    """
    Sets the reconnect settings.  Set retry_count to 0 to disable reconnecting.
    """


def obs_output_get_total_bytes(output: Output) -> int: ...


def obs_output_get_frames_dropped(output: Output) -> int: ...


def obs_output_get_total_frames(output: Output) -> int: ...


def obs_output_set_preferred_size(output: Output, width: int, height: int) -> None:
    """
    Sets the preferred scaled resolution for this output. Set width and height
    to 0 to disable scaling.

    If this output uses an encoder, it will call obs_encoder_set_scaled_size on
    the encoder before the stream is started. If the encoder is already active,
    then this function will trigger a warning and do nothing.
    """


def obs_output_get_width(output: Output) -> int:
    """
    For video outputs, returns the width of the encoded image
    """


def obs_output_get_height(output: Output) -> int:
    """
    For video outputs, returns the height of the encoded image
    """


def obs_output_get_id(output: Output) -> int: ...


# def obs_output_caption

def obs_output_caption_text1(output: Output, text: str) -> None: ...


def obs_output_caption_text2(output: Output, text: str, duration: float) -> None: ...


def obs_output_get_congestion(output: Output) -> float: ...


def obs_output_get_connect_time_ms(output: Output) -> int: ...


def obs_output_reconnecting(output: Output) -> bool: ...


def obs_output_set_last_error(output: Output, message: str) -> None: ...


def obs_output_get_last_error(output: Output) -> str: ...


def obs_output_get_supported_video_codecs(output: Output) -> str: ...


def obs_output_get_supported_audio_codecs(output: Output) -> str: ...


# Encoders

def obs_encoder_get_display_name(id: str) -> str: ...


def obs_video_encoder_create(id: str, name: str, settings: Data, hotkeys: Data) -> Encoder:
    """
    Creates a video encoder context
    :param id: Video encoder ID
    :param name: Name to assign to this context
    :param settings: Settings
    :return: The video encoder context, or NULL if failed or not found.
    """


def obs_audio_encoder_create(id: str, name: str, settings: Data, mixer: int, data: Data) -> Encoder:
    """
    Creates an audio encoder context
    :param id: Audio Encoder ID
    :param name: Name to assign to this context
    :param settings: Settings
    :param mixer: Index of the mixer to use for this audio encoder
    :return: The audio encoder context, or NULL if failed or not found.
    """


def obs_encoder_release(encoder: Encoder) -> None: ...


def obs_weak_encoder_addref(weak: WeakRef[Encoder]) -> None: ...


def obs_weak_encoder_release(weak: WeakRef[Encoder]) -> None: ...


def obs_encoder_get_ref(encoder: Encoder) -> Encoder: ...


def obs_encoder_get_weak_encoder(encoder: Encoder) -> WeakRef[Encoder]: ...


def obs_weak_encoder_get_encoder(weak: WeakRef[Encoder]) -> Encoder: ...


def obs_weak_encoder_references_encoder(weak: WeakRef[Encoder], encoder: Encoder) -> bool: ...


def obs_encoder_set_name(encoder: Encoder, name: str) -> None: ...


def obs_encoder_get_name(encoder: Encoder) -> str: ...


def obs_get_encoder_codec(id: str) -> str:
    """
    Returns the codec of an encoder by the id
    """


def obs_get_encoder_type(id: str) -> EncoderType:
    """
    Returns the type of an encoder by the id
    """


def obs_encoder_get_codec(encoder: Encoder) -> str:
    """
    Returns the codec of the encoder
    """


def obs_encoder_get_type(encoder: Encoder) -> EncoderType:
    """
    Returns the type of an encoder
    """


def obs_encoder_set_scaled_size(encoder: Encoder, width: int, height: int) -> None:
    """
    Sets the scaled resolution for a video encoder. Set width and height to 0 to disable scaling. If the encoder
    is active, this function will trigger a warning, and do nothing.
    """


def obs_encoder_scaling_enabled(encoder: Encoder) -> bool:
    """
    For video encoders, returns true if pre-encode scaling is enabled
    """


def obs_encoder_get_width(encoder: Encoder) -> int:
    """
    For video encoders, returns the width of the encoded image
    """


def obs_encoder_get_height(encoder: Encoder) -> int:
    """
    For video encoders, returns the height of the encoded image
    """


def obs_encoder_get_sample_rate(encoder: Encoder) -> int:
    """
    For audio encoders, returns the sample rate of the audio
    """


def obs_encoder_get_frame_size(encoder: Encoder) -> int:
    """
    For audio encoders, returns the frame size of the audio packet
    """


def obs_encoder_set_preferred_video_format(encoder: Encoder, format: VideoFormat) -> None:
    """
    Sets the preferred video format for a video encoder. If the encoder can use the format specified, it will
    force a conversion to that format if the obs output format does not match the preferred format.

    If the format is set to VIDEO_FORMAT_NONE, will revert to the default functionality of converting only when
    absolutely necessary.
    """


def obs_encoder_get_preferred_video_format(encoder: Encoder) -> VideoFormat: ...


def obs_encoder_defaults(id: str) -> Data:
    """
    Gets the default settings for an encoder type
    """


def obs_encoder_get_defaults(encoder: Encoder) -> Data:
    """
    Gets the default settings for an encoder type
    """


def obs_get_encoder_properties(id: str) -> Properties:
    """
    Returns the property list, if any. Free with obs_properties_destroy
    """


def obs_encoder_properties(encoder: Encoder) -> Properties:
    """
    Returns the property list of an existing encoder, if any. Free with obs_properties_destroy
    """


def obs_encoder_update(encoder: Encoder, settings: Data):
    """
    Updates the settings of the encoder context. Usually used for changing bitrate while active
    """


def obs_encoder_get_settings(encoder: Encoder) -> Data:
    """
    Returns the current settings for this encoder
    """


# def obs_encoder_set_video
# def obs_encoder_set_audio
# def obs_encoder_video
# def obs_encoder_audio

def obs_encoder_active(encoder: Encoder) -> bool:
    """
    Returns true if encoder is active, false otherwise
    """


def obs_encoder_get_id(encoder: Encoder) -> str: ...


def obs_get_encoder_caps(id: str) -> int: ...


def obs_encoder_get_caps(encoder: Encoder) -> int: ...


def obs_encoder_pause(encoder: Encoder) -> bool:
    """
    Returns whether encoder is paused
    """


def obs_encoder_get_last_error(encoder: Encoder) -> str: ...


def obs_encoder_set_last_error(encoder: Encoder) -> str: ...


def obs_encoder_get_pause_offset(encoder: Encoder) -> int: ...


# Stream Services

def obs_service_get_display_name(id: str) -> str: ...


def obs_service_create(id: str, name: str, settings: Data, hotkeys: Data) -> Service: ...


def obs_service_create_private(id: str, name: str, settings: Data) -> Service: ...


def obs_service_release(service: Service) -> None: ...


def obs_weak_service_addref(weak: WeakRef[Service]) -> None: ...


def obs_weak_service_release(weak: WeakRef[Service]) -> None: ...


def obs_service_get_ref(service: Service) -> Service: ...


def obs_service_get_weak_service(service: Service) -> WeakRef[Service]: ...


def obs_weak_service_get_service(weak: WeakRef[Service]) -> Service: ...


def obs_service_get_name(service: Service) -> str: ...


def obs_service_defaults(id: str) -> Data:
    """
    Gets the default settings for a service
    """


def obs_get_service_properties(id: str) -> Properties:
    """
    Returns the property list, if any. Free with obs_properties_destroy
    """


def obs_service_properties(service: Service) -> Properties:
    """
    Returns the property list, if any. Free with obs_properties_destroy
    """


def obs_service_get_type(service: Service) -> str:
    """
    Gets the service type
    """


def obs_service_update(service: Service, settings: Settings) -> None:
    """
    Updates the settings of the service context
    """


def obs_service_get_settings(service: Service) -> Data:
    """
    Returns the current settings for this service
    """


def obs_service_get_url(service: Service) -> str:
    """
    Returns the URL for this service context
    """


def obs_service_get_key(service: Service) -> str:
    """
    Returns the stream key (if any) for this service context
    """


def obs_service_get_username(service: Service) -> str:
    """
    Returns the username (if any) for this service context
    """


def obs_service_get_password(service: Service) -> str:
    """
    Returns the password (if any) for this service context
    """


def obs_service_apply_encoder_settings(service: Service, video_encoder_settings: Optional[Data],
                                       audio_encoder_settings: Optional[Data]) -> None:
    """
    Applies service-specific video encoder settings.

    :param video_encoder_settings: Video encoder settings.  Optional.
    :param audio_encoder_settings: Audio encoder settings.  Optional.
    """


def obs_service_get_id(service: Service) -> str: ...


def obs_service_get_supported_video_codecs(service: Service) -> list[str]: ...


def obs_service_get_output_type(service: Service) -> str: ...


def obs_frontend_get_scene_names() -> list[str]: ...


def obs_frontend_get_scenes() -> list[Source]: ...


def obs_frontend_get_current_scene() -> Optional[Source]: ...


def obs_frontend_set_current_scene(source: Source): ...


def obs_frontend_get_transitions() -> list[Source]: ...


def obs_frontend_get_current_transition() -> Optional[Source]: ...


def obs_frontend_set_current_transition(source: Source) -> None: ...


def obs_frontend_get_transition_duration() -> int: ...


def obs_frontend_set_transition_duration(duration: int) -> None: ...


def obs_frontend_release_tbar() -> None: ...


def obs_frontend_set_tbar_position(position: int) -> None: ...


def obs_frontend_get_tbar_position() -> int: ...


def obs_frontend_get_scene_collections() -> list[str]: ...


def obs_frontend_get_current_scene_collection() -> str: ...


def obs_frontend_set_current_scene_collection(name: str) -> None: ...


def obs_frontend_add_scene_collection(name: str) -> bool: ...


def obs_frontend_get_profiles() -> list[str]: ...


def obs_frontend_get_current_profile() -> str: ...


def obs_frontend_get_current_profile_path() -> str: ...


def obs_frontend_set_current_profile(name: str) -> None: ...


def obs_frontend_create_profile(name: str) -> None: ...


def obs_frontend_duplicate_profile(name: str) -> None: ...


def obs_frontend_delete_profile(profile: Profile) -> None: ...


def obs_frontend_remove_save_callback(callback: Callable[[Data, bool], None]) -> None: ...


def obs_frontend_add_save_callback(callback: Callable[[Data, bool], None]) -> None: ...


def obs_frontend_remove_event_callback(callback: Callable[[FrontendEvent], None]): ...


def obs_frontend_add_event_callback(callback: Callable[[FrontendEvent], None]): ...


def obs_frontend_streaming_start() -> None: ...


def obs_frontend_streaming_stop() -> None: ...


def obs_frontend_streaming_active() -> bool: ...


def obs_frontend_recording_start() -> None: ...


def obs_frontend_recording_stop() -> None: ...


def obs_frontend_recording_active() -> bool: ...


def obs_frontend_recording_pause() -> None: ...


def obs_frontend_recording_paused() -> bool: ...


def obs_frontend_recording_split_file() -> None: ...


def obs_frontend_replay_buffer_start() -> None: ...


def obs_frontend_replay_buffer_save() -> None: ...


def obs_frontend_replay_buffer_stop() -> None: ...


def obs_frontend_replay_buffer_active() -> bool: ...


# def obs_frontend_open_projector
def obs_frontend_save() -> None: ...


def obs_frontend_defer_save_begin() -> None: ...


def obs_frontend_defer_save_end() -> None: ...


def obs_frontend_get_streaming_output() -> Output: ...


def obs_frontend_get_recording_output() -> Output: ...


def obs_frontend_get_replay_buffer_output() -> Output: ...


# def obs_frontend_get_profile_config
# def obs_frontend_get_global_config

def obs_frontend_set_streaming_service(service: Service): ...


def obs_frontend_get_streaming_service() -> Service: ...


def obs_frontend_save_streaming_service() -> None: ...


def obs_frontend_preview_program_mode_active() -> bool: ...


def obs_frontend_set_preview_program_mode(enable: bool) -> None: ...


def obs_frontend_preview_program_trigger_transition() -> None: ...


def obs_frontend_set_preview_enabled(enable: bool) -> None: ...


def obs_frontend_preview_enabled() -> bool: ...


def obs_frontend_get_current_preview_scene() -> Source: ...


def obs_frontend_set_current_preview_scene(source: Source) -> None: ...


def obs_frontend_take_screenshot() -> None: ...


def obs_frontend_take_source_screenshot(source: Source) -> None: ...


def obs_frontend_get_virtualcam_output() -> Output: ...


def obs_frontend_start_virtualcam() -> None: ...


def obs_frontend_stop_virtualcam() -> None: ...


def obs_frontend_virtualcam_active() -> bool: ...


def obs_frontend_reset_video() -> None: ...


def obs_frontend_open_source_properties(source: Source) -> None: ...


def obs_frontend_open_source_filters(source: Source) -> None: ...


def obs_frontend_open_source_interaction(source: Source) -> None: ...


def obs_frontend_get_current_record_output_path() -> str: ...


def obs_frontend_get_locale_string(string: str) -> str: ...


def obs_frontend_is_theme_dark() -> bool: ...


def obs_frontend_get_last_recording() -> str: ...


def obs_frontend_get_last_screenshot() -> str: ...


def obs_frontend_get_last_replay() -> str: ...


def media_frames_per_second_to_frame_interval(fps: MediaFramesPerSecond) -> float: ...


def media_frames_per_second_to_fps(fps: MediaFramesPerSecond) -> float: ...


def media_frames_per_second_is_valid(fps: MediaFramesPerSecond) -> bool: ...


def obs_properties_create() -> Properties:
    """
    :return: A new properties object.
    """


def obs_properties_destroy(props: Properties) -> None: ...


def obs_properties_get_flags(props: Properties) -> int:
    """
    :return: 0 or a bitwise OR combination of one of the following values:
             OBS_PROPERTIES_DEFER_UPDATE - A hint that tells the front-end to defers updating the settings until
             the user has finished editing all properties rather than immediately updating any settings
    """


def obs_properties_set_flags(props: Properties, flags: int) -> None:
    """
    :param flags: 0 or a bitwise OR combination of one of the following values:
                  OBS_PROPERTIES_DEFER_UPDATE - A hint that tells the front-end to defers updating the settings
                  until the user has finished editing all properties rather than immediately updating any settings
    """


def obs_properties_first(props: Properties) -> Optional[Property]:
    """
    :return: The first property in the properties object
    """


def obs_properties_get(props: Properties, property: str) -> Optional[Property]:
    """
    :param property: The name of the property to get
    :return: A specific property or None if not found
    """


def obs_properties_get_parent(props: Properties) -> Optional[Properties]: ...


def obs_properties_remove_by_name(props: Properties, property: str) -> None: ...


def obs_properties_apply_settings(props: Properties, settings: Data) -> None:
    """
    Applies settings to the properties by calling all the necessary modification callbacks
    """


# Property Metadata
def obs_property_name(property: Property) -> str:
    """
    :return: The setting identifier string of the property
    """


def obs_property_set_description(property: Property, description: str) -> None:
    """
    Sets the displayed localized name of the property, shown to the user.
    """


def obs_property_description(property: Property) -> str:
    """
    :return: The actual localized display name of the property
    """


def obs_property_set_long_description(property: Property, long_description: str) -> None:
    """
    Sets the localized long description of the property, usually shown to a user via tooltip.
    """


def obs_property_long_description(property: Property) -> str:
    """
    :return: A detailed description of what the setting is used for. Usually used with things like tooltips.
    """


def obs_property_get_type(property: Property) -> PropertyType:
    """
    :return: See :class:PropertyType
    """


def obs_property_enabled(property: Property) -> bool: ...


def obs_property_set_enabled(property: Property, enabled: bool) -> None: ...


def obs_property_visible(property: Property) -> bool: ...


def obs_property_set_visible(property: Property, visible: bool) -> None: ...


def obs_property_set_modified_callback(
        properties: Properties, property: Property,
        callback: Callable[[Properties, Property, Settings], bool]) -> None:
    """
    Allows the ability to change the properties depending on what settings are used by the user.

    The callback should return true if the property widgets need to be refreshed due to changes to the property
    layout.
    """


def obs_property_modified(property: Property, settings: Data) -> bool: ...


# Bool Properties
def obs_properties_add_bool(
        props: Properties, name: str, description: str) -> Property:
    """
    Adds a boolean property.
    :param name: Setting identifier string
    :param description: Localized name shown to user
    :return: The property
    """


# Int Properties
def obs_properties_add_int(
        props: Properties, name: str, description: str,
        min: int, max: int, step: int) -> Property:
    """
    Adds an integer property.
    :param name: Setting identifier string
    :param description: Localized name shown to user
    :param min: Minimum value
    :param max: Maximum value
    :param step: Step value
    :return: The property
    """


def obs_properties_add_int_slider(
        props: Properties, name: str, description: str,
        min: int, max: int, step: int) -> Property:
    """
    Adds an integer property.
    :param name: Setting identifier string
    :param description: Localized name shown to user
    :param min: Minimum value
    :param max: Maximum value
    :param step: Step value
    :return: The property
    """


def obs_property_int_type(property: Property) -> NumberType: ...


def obs_property_int_min(property: Property) -> int: ...


def obs_property_int_max(property: Property) -> int: ...


def obs_property_int_step(property: Property) -> int: ...


def obs_property_int_set_limits(property: Property, min: int, max: int, step: int) -> None: ...


def obs_property_int_suffix(property: Property) -> str: ...


def obs_property_int_set_suffix(property: Property, suffix: str) -> None: ...


# Float Properties
def obs_properties_add_float(
        props: Properties, name: str, description: str,
        min: float, max: float, step: float) -> Property:
    """
    Adds a float property.
    :param name: Setting identifier string
    :param description: Localized name shown to user
    :param min: Minimum value
    :param max: Maximum value
    :param step: Step value
    :return: The property
    """


def obs_properties_add_float_slider(
        props: Properties, name: str, description: str,
        min: float, max: float, step: float) -> Property:
    """
    Adds a float property.
    :param name: Setting identifier string
    :param description: Localized name shown to user
    :param min: Minimum value
    :param max: Maximum value
    :param step: Step value
    :return: The property
    """


def obs_property_float_type(property: Property) -> NumberType: ...


def obs_property_float_min(property: Property) -> float: ...


def obs_property_float_max(property: Property) -> float: ...


def obs_property_float_step(property: Property) -> float: ...


def obs_property_float_set_limits(property: Property, min: float, max: float, step: float) -> None: ...


def obs_property_float_suffix(property: Property) -> str: ...


def obs_property_float_set_suffix(property: Property, suffix: str) -> None: ...


# Text Properties
def obs_properties_add_text(
        props: Properties, name: str, description: str,
        type: TextType) -> Property:
    """
    Adds a text property.
    :param name: Setting identifier string
    :param description: Localized name shown to user
    :param type: See :class:TextType
    :return: The property
    """


def obs_property_text_type(property: Property) -> TextType: ...


def obs_property_text_monospace(property: Property) -> bool: ...


def obs_property_text_set_monospace(property: Property, monospace: bool) -> None: ...


def obs_property_text_info_type(property: Property) -> TextInfoType: ...


def obs_property_text_set_info_type(property: Property, type: TextInfoType) -> None: ...


def obs_property_text_info_word_wrap(property: Property) -> bool: ...


def obs_property_text_set_info_word_wrap(property: Property, word_wrap: bool) -> None: ...


# Path Properties
def obs_properties_add_path(
        props: Properties, name: str, description: str,
        type: PathType, filter: str, default_path: str) -> Property:
    """
    Adds a ‘path’ property. Can be a directory or a file.

    If target is a file path, the filters should be this format, separated by double semicolons, and extensions
    separated by space::

        "Example types 1 and 2 (*.ex1 *.ex2);;Example type 3 (*.ex3)"

    :param name: Setting identifier string
    :param description: Localized name shown to user
    :param type: See :class:PathType
    :param filter: If type is a file path, then describes the file filter that the user can browse. Items are
                   separated via double semicolons. If multiple file types in a filter, separate with space.
    :param default_path: The default path to start in, or None
    :return: The property
    """
    pass


def obs_property_path_type(property: Property) -> PathType: ...


def obs_property_path_filter(property: Property) -> str: ...


def obs_property_path_default_path(property: Property) -> str: ...


# List Properties
def obs_properties_add_list(
        props: Properties, name: str, description: str,
        type: ComboType, format: ComboFormat) -> Property:
    """
    Adds an integer/string/floating point item list. This would be implemented as a combo box in user interface.
    :param name: Setting identifier string
    :param description: Localized name shown to user
    :param type: See :class:ComboType
    :param format: See :class:ComboFormat
    :return: The property
    """


def obs_property_list_type(property: Property) -> ComboType: ...


def obs_property_list_format(property: Property) -> ComboFormat: ...


def obs_property_list_clear(property: Property) -> None: ...


def obs_property_list_add_string(property: Property, name: str, val: str) -> int: ...


def obs_property_list_add_int(property: Property, name: str, val: int) -> int: ...


def obs_property_list_add_float(property: Property, name: str, val: float) -> int: ...


def obs_property_list_insert_string(property: Property, idx: int, name: str, val: str) -> None: ...


def obs_property_list_insert_int(property: Property, idx: int, name: str, val: int) -> None: ...


def obs_property_list_insert_float(property: Property, idx: int, name: str, val: float) -> None: ...


def obs_property_list_item_disable(property: Property, idx: int, disabled: bool) -> None: ...


def obs_property_list_item_disabled(property: Property, idx: int) -> bool: ...


def obs_property_list_item_remove(property: Property, idx: int) -> None: ...


def obs_property_list_item_count(property: Property) -> int: ...


def obs_property_list_item_name(property: Property, idx: int) -> str: ...


def obs_property_list_item_int(property: Property, idx: int) -> int: ...


def obs_property_list_item_float(property: Property, idx: int) -> float: ...


# Color Properties
def obs_properties_add_color(
        props: Properties, name: str, description: str) -> Property:
    """
    Adds a color property without alpha (stored internally with an alpha value of 255). The color can be retrieved
    from an Data object by using obs_data_get_int().
    :param name: Setting identifier string
    :param description: Localized name shown to user
    :return: The property
    """


def obs_properties_add_color_alpha(
        props: Properties, name: str, description: str) -> Property:
    """
    Adds a color property with alpha. The color can be retrieved from an Data object by using obs_data_get_int().
    :param name: Setting identifier string
    :param description: Localized name shown to user
    :return: The property
    """


# Button Properties
def obs_properties_add_button(
        properties: Properties, name: str, text: str,
        callback: Callable[[Properties, Property], bool]) -> Property:
    """
    Adds a button property to an Properties object.
    The callback takes two parameters: the first parameter is the Properties object, and the second parameter
    is the Property for the button.
    :param properties: An Properties object.
    :param name: A setting identifier string.
    :param text: Button text.
    :param callback: Button callback. This callback is automatically cleaned up.
    :return: The newly created Property
    """


def obs_property_button_type(property: Property) -> ButtonType: ...


def obs_property_button_set_type(property: Property, type: ButtonType) -> None: ...


def obs_property_button_url(property: Property) -> str: ...


def obs_property_button_set_url(property: Property, url: str) -> None: ...


# Font Properties
def obs_properties_add_font(
        props: Properties, name: str, description: str) -> Property:
    """
    Adds a font property. The font can be retrieved from an Data object by using obs_data_get_obj().
    :param name: Setting identifier string
    :param description: Localized name shown to user
    :return: The property
    """


# Editable List Properties
def obs_properties_add_editable_list(
        props: Properties, name: str, description: str,
        type: EditableListType, filter: str, default_path: str) -> Property:
    """
    Adds a list in which the user can add/insert/remove items. The items can be retrieved from an Data object by
    using obs_data_get_array().
    :param name: Setting identifier string
    :param description: Localized name shown to user
    :param type: See :class:EditableListType
    :param filter: File filter to use if a file list
    :param default_path: Default path if a file list
    :return: The property
    """


def obs_property_editable_list_type(property: Property) -> EditableListType: ...


def obs_property_editable_list_filter(property: Property) -> str: ...


def obs_property_editable_list_default_path(property: Property) -> str: ...


# FPS Properties
def obs_properties_add_frame_rate(
        props: Properties, name: str, description: str) -> Property:
    """
    Adds a frame rate property.
    :param name: Setting identifier string
    :param description: Localized name shown to user
    :return: The property
    """


def obs_property_frame_rate_clear(property: Property) -> None: ...


def obs_property_frame_rate_options_clear(property: Property) -> None: ...


def obs_property_frame_rate_fps_ranges_clear(property: Property) -> None: ...


def obs_property_frame_rate_option_add(
        property: Property, name: str, description: str) -> int: ...


def obs_property_frame_rate_fps_range_add(
        property: Property, min: MediaFramesPerSecond, max: MediaFramesPerSecond) -> int: ...


def obs_property_frame_rate_option_insert(
        property: Property, idx: int, name: str, description: str) -> None: ...


def obs_property_frame_rate_fps_range_insert(
        property: Property, idx: int, min: MediaFramesPerSecond, max: MediaFramesPerSecond) -> None: ...


def obs_property_frame_rate_options_count(property: Property) -> int: ...


def obs_property_frame_rate_option_name(property: Property, idx: int) -> str: ...


def obs_property_frame_rate_option_description(property: Property, idx: int) -> str: ...


def obs_property_frame_rate_fps_ranges_count(property: Property) -> int: ...


def obs_property_frame_rate_fps_range_min(property: Property, idx: int) -> MediaFramesPerSecond: ...


def obs_property_frame_rate_fps_range_max(property: Property, idx: int) -> MediaFramesPerSecond: ...


# Property Groups
def obs_properties_add_group(
        props: Properties, name: str, description: str,
        type: GroupType, group: Properties) -> Property:
    """
    Adds a property group.
    :param name: Setting identifier string
    :param description: Localized name shown to user
    :param type: See :class:GroupType
    :param group: Group to add
    :return: The property
    """


def obs_property_group_type(property: Property) -> GroupType: ...


def obs_property_group_content(property: Property) -> Properties: ...


def script_log_no_endl(*args) -> None: ...


def script_log(*args) -> None: ...


def timer_remove(callback: Callable[[], None]) -> None:
    """
    Removes a timer callback.

    Note: You can also use remove_current_callback() to terminate the timer from the timer callback.
    :param callback: Callback to be removed
    """


def timer_add(callback: Callable[[], None], interval: int) -> None:
    """
    Triggers a timer callback with the given interval.
    :param callback: Callback to be triggered
    :param interval: Interval in milliseconds
    """


def calldata_source(calldata: CallData, name: str) -> Source:
    """
    Casts a pointer parameter of an CallData object to an Source object.
    :param calldata: An CallData object
    :param name: Name of the parameter.
    :return: A borrowed reference to an Source object.
    """


def calldata_sceneitem(calldata: CallData, name: str) -> SceneItem:
    """
    Casts a pointer parameter of an CallData object to an SceneItem object.
    :param calldata: An CallData object
    :param name: Name of the parameter.
    :return: A borrowed reference to an SceneItem object.
    """


def source_list_release(source_list: list[Source]) -> None:
    """
    Releases the references of a source list.
    :param source_list: Array of sources to release.
    """


def sceneitem_list_release(item_list: list[SceneItem]) -> None:
    """
    Releases the references of a scene item list.
    :param item_list: Array of scene items to release.
    """
    pass


def obs_enum_sources() -> list[Source]:
    """
    Enumerates all sources.
    :return: An array of reference-incremented sources.
             Release with source_list_release().
    """


def obs_scene_enum_items(scene: Source) -> list[SceneItem]:
    """
    Enumerates scene items within a scene.
    :param scene: object to enumerate items from.
    :return: List of scene items.
             Release with sceneitem_list_release().
    """
    pass


def obs_sceneitem_group_enum_items(group: SceneItem):
    """
    Enumerates scene items within a group.
    :param group: object to enumerate items from.
    :return: list of scene items.
             Release with sceneitem_list_release().
    """
    pass


def obs_remove_tick_callback(callback: Callable[[float], None]) -> None:
    """
    Removes a tick callback.
    :param callback: Callback to be removed
    """


def obs_add_tick_callback(callback: Callable[[float], None]) -> None:
    """
    Triggers a callback on every tick.
    :param callback: Callback to be triggered
    """


# def signal_handler_disconnect(handler: any, signal: str, callback: Callable[[any], None]):
#    pass

# def signal_handler_connect(*args):
#    pass

# def signal_handler_disconnect_global(*args):
#    pass

# def signal_handler_connect_global(*args):
#    pass

def obs_hotkey_unregister(callback: Callable[[bool], None]) -> None:
    """
    Unregisters the hotkey associated with the specified callback.
    :param callback: Callback of the hotkey to unregister.
    """


def obs_hotkey_register_frontend(
        name: str, description: str,
        callback: Callable[[bool], None]) -> int:
    """
    Adds a frontend hotkey.
    The callback takes one parameter: a boolean ‘pressed’ parameter.
    :param name: Unique name identifier string of the hotkey.
    :param description: Hotkey description shown to the user.
    :param callback: Callback for the hotkey.
           Use obs_hotkey_unregister() or remove_current_callback() to remove the callback.
    :return: The newly generated id of the hotkey.
    """


def remove_current_callback() -> None:
    """
    Removes the current callback being executed. Does nothing if not within a callback.
    """
