# Copyright: (c) 2023 Jordan Borean (@jborean93) <jborean93@gmail.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import annotations

import sspi


def test_query_session_keys(
    authenticated_contexts: tuple[sspi.InitiatorSecurityContext, sspi.AcceptorSecurityContext],
) -> None:
    c_actual = sspi.query_context_attributes(authenticated_contexts[0], sspi.SecPkgContextSessionKey)
    assert isinstance(c_actual, sspi.SecPkgContextSessionKey)
    assert isinstance(c_actual.session_key, bytes)

    s_actual = sspi.query_context_attributes(authenticated_contexts[1], sspi.SecPkgContextSessionKey)
    assert isinstance(s_actual, sspi.SecPkgContextSessionKey)
    assert isinstance(s_actual.session_key, bytes)

    assert c_actual.session_key == s_actual.session_key
    assert repr(c_actual) == repr(s_actual)


def test_query_names(
    authenticated_contexts: tuple[sspi.InitiatorSecurityContext, sspi.AcceptorSecurityContext],
) -> None:
    c_actual = sspi.query_context_attributes(authenticated_contexts[0], sspi.SecPkgContextNames)
    assert isinstance(c_actual, sspi.SecPkgContextNames)
    assert isinstance(c_actual.username, str)

    s_actual = sspi.query_context_attributes(authenticated_contexts[1], sspi.SecPkgContextNames)
    assert isinstance(s_actual, sspi.SecPkgContextNames)
    assert isinstance(s_actual.username, str)

    assert c_actual.username == s_actual.username
    assert repr(c_actual) == repr(s_actual)


def test_query_sizes(
    authenticated_contexts: tuple[sspi.InitiatorSecurityContext, sspi.AcceptorSecurityContext],
) -> None:
    c_actual = sspi.query_context_attributes(authenticated_contexts[0], sspi.SecPkgContextSizes)
    assert isinstance(c_actual, sspi.SecPkgContextSizes)
    assert isinstance(c_actual.max_signature, int)
    assert isinstance(c_actual.max_token, int)
    assert isinstance(c_actual.block_size, int)
    assert isinstance(c_actual.security_trailer, int)

    s_actual = sspi.query_context_attributes(authenticated_contexts[1], sspi.SecPkgContextSizes)
    assert isinstance(s_actual, sspi.SecPkgContextSizes)
    assert isinstance(s_actual.max_signature, int)
    assert isinstance(s_actual.max_token, int)
    assert isinstance(s_actual.block_size, int)
    assert isinstance(s_actual.security_trailer, int)

    assert c_actual.max_signature == s_actual.max_signature
    assert c_actual.max_token == s_actual.max_token
    assert c_actual.block_size == s_actual.block_size
    assert c_actual.security_trailer == s_actual.security_trailer
    assert repr(c_actual) == repr(s_actual)
