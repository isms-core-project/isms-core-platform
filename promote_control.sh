#!/bin/bash
# ─────────────────────────────────────────────────────────────────────────────
# promote_control.sh
# Syncs QA'd controls from factory_claude_ai → factory_isms (GitHub repo)
#
# SOURCES:
#   50-isms-core-framework/  → isms-core-framework/
#   10-isms-core-operational/ → isms-core-operational/
#   51-isms-core-privacy/    → isms-core-privacy/
#   52-isms-core-cloud/iso27018-pii-cloud     → isms-core-cloud/
#   52-isms-core-cloud/iso27017-sec-cloud     → isms-core-sec/   (future)
#   53-isms-core-ai/         → isms-core-ai/
#
# TARGET STRUCTURE (subdirectory split):
#   factory_isms/
#   ├── isms-core-framework/
#   │   ├── 00-foundation-policies/
#   │   ├── A.5-organizational-controls/
#   │   │   └── isms-a.5.X-control-name/
#   │   │       ├── POL/  ├── IMP/  ├── SCR/  ├── REF/  ├── CTX/  ├── FORM/  └── WKBK/
#   │   ├── A.6-people-controls/
#   │   ├── A.7-physical-controls/
#   │   └── A.8-technological-controls/
#   ├── isms-core-operational/
#   │   ├── A.5-organizational-controls/
#   │   │   └── isms-a.5.X-control-name/
#   │   │       └── POL/   (one OP-POL per control group)
#   │   ├── A.6-people-controls/
#   │   ├── A.7-physical-controls/
#   │   └── A.8-technological-controls/
#   ├── isms-core-privacy/    (ISO 27701:2025 — Privacy Extension)
#   │   ├── 00-checklist-engine/
#   │   ├── 00-priv-foundation-policies/
#   │   ├── privacy-controller/
#   │   ├── privacy-processor/
#   │   └── privacy-shared/
#   ├── isms-core-cloud/      (ISO 27018:2025 — PII in Cloud)
#   │   ├── iso27017-sec-cloud/
#   │   └── iso27018-pii-cloud/
#   └── isms-core-sec/        (ISO 27017:2025 — future, not yet built)
#
# QA GATE LOGIC:
#   POLs  (.md in POL/)   → ALL must have <!-- QA_VERIFIED: -->  → sync
#   IMPs  (.md in IMP/)   → ALL must have <!-- QA_VERIFIED: -->  → sync
#   SCRs  (.py in SCR/)   → ALL must contain QA_VERIFIED         → sync
#   REFs  (.md in REF/)   → ALL must have <!-- QA_VERIFIED: -->  → sync
#   CTX   (.md in CTX/)   → ALL must have <!-- QA_VERIFIED: -->  → sync
#   FORM  (.md in FORM/)  → ALL must have <!-- QA_VERIFIED: -->  → sync
#   WKBK  (WKBK/)         → No QA gate — synced if exists        → sync
#
# USAGE:
#   ./promote_control.sh isms-a.8.24-use-of-cryptography
#   ./promote_control.sh --dry-run isms-a.8.24-use-of-cryptography
#   ./promote_control.sh --all
#   ./promote_control.sh --dry-run --all
#   ./promote_control.sh --status
#   ./promote_control.sh --operational           # Promote all OP-POLs
#   ./promote_control.sh --dry-run --operational  # Dry run OP-POL promotion
#   ./promote_control.sh --privacy               # Promote Privacy product (ISO 27701:2025)
#   ./promote_control.sh --cloud                 # Promote Cloud product (ISO 27018:2025)
#   ./promote_control.sh --sec                   # Promote SEC product (ISO 27017:2025 — future)
#   ./promote_control.sh --ai                    # Promote AI product (ISO/IEC 42001:2023)
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail

# ─── CONFIGURE THESE ─────────────────────────────────────────────────────────
DEV="${HOME}/Files/Factory/factory_claude_ai"
FW_SRC="$DEV/50-isms-core-framework"
PROD_ROOT="${HOME}/Files/Factory/factory_isms"
FW_DEST="${PROD_ROOT}/isms-core-framework"
OP_SRC="$DEV/10-isms-core-operational"
OP_DST="${PROD_ROOT}/isms-core-operational"
PRIV_SRC="$DEV/51-isms-core-privacy"
PRIV_DST="${PROD_ROOT}/isms-core-privacy"
CLD_SRC="$DEV/52-isms-core-cloud/iso27018-pii-cloud"
CLD_DST="${PROD_ROOT}/isms-core-cloud"
SEC_SRC="$DEV/52-isms-core-cloud/iso27017-sec-cloud"
SEC_DST="${PROD_ROOT}/isms-core-sec"
AI_SRC="$DEV/53-isms-core-ai"
AI_DEST="${PROD_ROOT}/isms-core-ai"

# ─── COLORS ──────────────────────────────────────────────────────────────────
R='\033[0;31m' G='\033[0;32m' Y='\033[1;33m' B='\033[0;34m' C='\033[0;36m' D='\033[2m' N='\033[0m'

# ─── RSYNC EXCLUDES ──────────────────────────────────────────────────────────
EXCL=(
    --exclude='__pycache__'   --exclude='*.pyc'
    --exclude='97_backup'     --exclude='98_originals'    --exclude='98_original'
    --exclude='99_archive'    --exclude='100_review'      --exclude='96_samples'
    --exclude='old_*'         --exclude='*_old'           --exclude='*_old_*'
    --exclude='backup_before_*'
    --exclude='30_copilot-audit'
    --exclude='.DS_Store'
)

# ─────────────────────────────────────────────────────────────────────────────
# FIND CONTROL IN FRAMEWORK
# Returns the full path to a control's directory in 50-isms-core-framework
# ─────────────────────────────────────────────────────────────────────────────
find_control_dir() {
    local control="$1"
    for section_dir in "$FW_SRC"/[0-9][0-9]-* "$FW_SRC"/A.*; do
        [ -d "$section_dir/$control" ] && { echo "$section_dir/$control"; return 0; }
    done
    return 1
}

# ─────────────────────────────────────────────────────────────────────────────
# GET CATEGORY (section directory name) FOR A CONTROL
# Derives category from the framework directory structure
# ─────────────────────────────────────────────────────────────────────────────
get_category() {
    local control="$1"
    for section_dir in "$FW_SRC"/[0-9][0-9]-* "$FW_SRC"/A.*; do
        [ -d "$section_dir/$control" ] && { basename "$section_dir"; return 0; }
    done
    echo "unknown"
}

# ─────────────────────────────────────────────────────────────────────────────
# QA CHECKS (paths for unified framework structure)
# All functions take the control's base directory as $1
# ─────────────────────────────────────────────────────────────────────────────

pol_qa_counts() {
    local dir="$1/POL"
    local pass=0 total=0
    [ -d "$dir" ] || { echo "0 0"; return; }
    for f in "$dir"/*.md; do
        [ -f "$f" ] || continue
        ((total++)) || true
        if grep -qF "<!-- QA_VERIFIED:" "$f"; then
            ((pass++)) || true
        fi
    done
    echo "$pass $total"
}

imp_qa_counts() {
    local dir="$1/IMP"
    local pass=0 total=0
    [ -d "$dir" ] || { echo "0 0"; return; }
    for f in "$dir"/*.md; do
        [ -f "$f" ] || continue
        ((total++)) || true
        if grep -qF "<!-- QA_VERIFIED:" "$f"; then
            ((pass++)) || true
        fi
    done
    echo "$pass $total"
}

scr_qa_counts() {
    local dir="$1/SCR"
    local pass=0 total=0
    [ -d "$dir" ] || { echo "0 0"; return; }
    while IFS= read -r -d '' f; do
        ((total++)) || true
        if grep -qF "QA_VERIFIED:" "$f"; then
            ((pass++)) || true
        fi
    done < <(find "$dir" -name '*.py' -not -path '*/__pycache__/*' -not -path '*/90_workbooks/*' -print0)
    echo "$pass $total"
}

ref_qa_counts() {
    local dir="$1/REF"
    local pass=0 total=0
    [ -d "$dir" ] || { echo "0 0"; return; }
    for f in "$dir"/*.md; do
        [ -f "$f" ] || continue
        ((total++)) || true
        if grep -qF "<!-- QA_VERIFIED:" "$f"; then
            ((pass++)) || true
        fi
    done
    echo "$pass $total"
}

ctx_qa_counts() {
    local dir="$1/CTX"
    local pass=0 total=0
    [ -d "$dir" ] || { echo "0 0"; return; }
    for f in "$dir"/*.md; do
        [ -f "$f" ] || continue
        ((total++)) || true
        if grep -qF "<!-- QA_VERIFIED:" "$f"; then
            ((pass++)) || true
        fi
    done
    echo "$pass $total"
}

form_qa_counts() {
    local dir="$1/FORM"
    local pass=0 total=0
    [ -d "$dir" ] || { echo "0 0"; return; }
    for f in "$dir"/*.md; do
        [ -f "$f" ] || continue
        ((total++)) || true
        if grep -qF "<!-- QA_VERIFIED:" "$f"; then
            ((pass++)) || true
        fi
    done
    echo "$pass $total"
}

ins_qa_counts() {
    local dir="$1/INS"
    local pass=0 total=0
    [ -d "$dir" ] || { echo "0 0"; return; }
    for f in "$dir"/*.md; do
        [ -f "$f" ] || continue
        ((total++)) || true
        if grep -qF "<!-- QA_VERIFIED:" "$f"; then
            ((pass++)) || true
        fi
    done
    echo "$pass $total"
}

# ─────────────────────────────────────────────────────────────────────────────
# CONTROL DISCOVERY (from unified framework)
# Iterates section directories in order: A.0, A.5, A.6, A.7, A.8
# ─────────────────────────────────────────────────────────────────────────────
get_controls() {
    for section_dir in "$FW_SRC"/[0-9][0-9]-* "$FW_SRC"/A.*; do
        [ -d "$section_dir" ] || continue
        for ctrl_dir in "$section_dir"/isms-*; do
            [ -d "$ctrl_dir" ] || continue
            local n=$(basename "$ctrl_dir")
            [[ "$n" == *x.xx* ]] && continue
            [[ "$n" == *sample* ]] && continue
            echo "$n"
        done
    done
}

# ─────────────────────────────────────────────────────────────────────────────
# DISPLAY NAME — shorter control name for terminal output
# ─────────────────────────────────────────────────────────────────────────────
short_name() {
    echo "$1" | sed 's/^isms-a\./A./' | sed 's/^isms-//'
}

# ─────────────────────────────────────────────────────────────────────────────
# RSYNC EXECUTOR (unified — one function for all types)
# ─────────────────────────────────────────────────────────────────────────────
sync_type() {
    local control="$1" type="$2" dry="$3"
    local ctrl_dir
    ctrl_dir=$(find_control_dir "$control") || return 0
    local category=$(get_category "$control")
    local src="$ctrl_dir/$type"
    local dst="$FW_DEST/$category/$control/$type"
    [ -d "$src" ] || return 0

    local flags=(-a --delete "${EXCL[@]}")
    [ "$dry" = "yes" ] && flags+=(-n)

    mkdir -p "$dst"
    rsync "${flags[@]}" "$src/" "$dst/" 2>&1 | sed 's/^/      /'
}

# ─────────────────────────────────────────────────────────────────────────────
# STATUS DASHBOARD
# ─────────────────────────────────────────────────────────────────────────────
cmd_status() {
    echo ""
    echo -e "${B}╔════════════════════════════════════════════════════════════════════════════════════════════════════════════╗${N}"
    echo -e "${B}║${N}                              ${C}ISMS CORE — QA & Promotion Status${N}                                            ${B}║${N}"
    echo -e "${B}╚════════════════════════════════════════════════════════════════════════════════════════════════════════════╝${N}"
    echo -e "  ${D}Source: 50-isms-core-framework/${N}"
    echo ""

    local ready=0 partial=0
    local current_category=""

    for ctrl in $(get_controls); do
        local category=$(get_category "$ctrl")
        local ctrl_dir
        ctrl_dir=$(find_control_dir "$ctrl") || continue

        # Print section header when it changes
        if [ "$category" != "$current_category" ]; then
            [ -n "$current_category" ] && echo ""
            echo -e "  ${B}━━━ $category ━━━${N}"
            current_category="$category"
        fi

        read pp pt <<< $(pol_qa_counts "$ctrl_dir")
        read ip it <<< $(imp_qa_counts "$ctrl_dir")
        read sp st <<< $(scr_qa_counts "$ctrl_dir")
        read rp rt <<< $(ref_qa_counts "$ctrl_dir")
        read cp ct <<< $(ctx_qa_counts "$ctrl_dir")
        read fp ft <<< $(form_qa_counts "$ctrl_dir")

        local pc ic sc rc cc fc
        if   [ $pt -eq 0 ]; then pc="${D}—${N}"
        elif [ $pp -eq $pt ]; then pc="${G}✅${N}"
        else                        pc="${R}⭕${N}"; fi

        if   [ $it -eq 0 ]; then ic="${D}—${N}"
        elif [ $ip -eq $it ]; then ic="${G}✅${N}"
        else                        ic="${R}⭕${N}"; fi

        if   [ $st -eq 0 ]; then sc="${D}—${N}"
        elif [ $sp -eq $st ]; then sc="${G}✅${N}"
        else                        sc="${R}⭕${N}"; fi

        if   [ $rt -eq 0 ]; then rc="${D}—${N}"
        elif [ $rp -eq $rt ]; then rc="${G}✅${N}"
        else                        rc="${R}⭕${N}"; fi

        if   [ $ct -eq 0 ]; then cc="${D}—${N}"
        elif [ $cp -eq $ct ]; then cc="${G}✅${N}"
        else                        cc="${R}⭕${N}"; fi

        if   [ $ft -eq 0 ]; then fc="${D}—${N}"
        elif [ $fp -eq $ft ]; then fc="${G}✅${N}"
        else                        fc="${R}⭕${N}"; fi

        local icon
        local has_any=false has_all_pass=true
        [ $pt -gt 0 ] && { has_any=true; [ $pp -ne $pt ] && has_all_pass=false; }
        [ $it -gt 0 ] && { has_any=true; [ $ip -ne $it ] && has_all_pass=false; }
        [ $st -gt 0 ] && { has_any=true; [ $sp -ne $st ] && has_all_pass=false; }
        [ $rt -gt 0 ] && { has_any=true; [ $rp -ne $rt ] && has_all_pass=false; }
        [ $ct -gt 0 ] && { has_any=true; [ $cp -ne $ct ] && has_all_pass=false; }
        [ $ft -gt 0 ] && { has_any=true; [ $fp -ne $ft ] && has_all_pass=false; }

        if [ "$has_any" = false ]; then
            continue
        elif [ "$has_all_pass" = true ]; then
            icon="${G}✅${N}"; ((ready++)) || true
        else
            icon="${Y}⚠ ${N}"; ((partial++)) || true
        fi

        local sn=$(short_name "$ctrl")
        printf "    %s %-50s  POL:%s IMP:%s SCR:%s REF:%s CTX:%s FORM:%s\n" "$icon" "$sn" "$pc" "$ic" "$sc" "$rc" "$cc" "$fc"
    done

    echo ""
    echo -e "  ${D}────────────────────────────────────────────────────────────────${N}"
    echo -e "  ${G}✅ Ready: $ready${N}    ${Y}⚠  Partial: $partial${N}"
    echo ""
}

# ─────────────────────────────────────────────────────────────────────────────
# PROMOTE SINGLE CONTROL
# ─────────────────────────────────────────────────────────────────────────────
cmd_promote() {
    local control="$1" dry="$2"
    local ctrl_dir
    ctrl_dir=$(find_control_dir "$control") || {
        echo -e "  ${R}Control not found in framework: $control${N}" >&2
        exit 1
    }
    local category=$(get_category "$control")

    echo ""
    echo -e "${B}════════════════════════════════════════════════════════════════════════════════${N}"
    echo -e "${B}  Promote: ${C}$control${N}"
    echo -e "${B}  Source:  ${C}$FW_SRC/$category/$control/${N}"
    echo -e "${B}  Target:  ${C}$FW_DEST/$category/$control/${N}"
    [ "$dry" = "yes" ] && echo -e "  ${Y}★ DRY RUN — nothing will be written ★${N}"
    echo -e "${B}════════════════════════════════════════════════════════════════════════════════${N}"
    echo ""

    local synced=0

    # ── POL ──
    if [ -d "$ctrl_dir/POL" ]; then
        read pp pt <<< $(pol_qa_counts "$ctrl_dir")
        if [ $pt -gt 0 ]; then
            if [ $pp -eq $pt ]; then
                echo -e "  ${C}POL${N}  ${G}QA ✅  $pp/$pt passed${N}"
                sync_type "$control" "POL" "$dry"
                ((synced++)) || true
            else
                echo -e "  ${C}POL${N}  ${R}QA ⭕  $pp/$pt — BLOCKED${N}"
            fi
        fi
    fi

    # ── IMP ──
    if [ -d "$ctrl_dir/IMP" ]; then
        read ip it <<< $(imp_qa_counts "$ctrl_dir")
        if [ $it -gt 0 ]; then
            if [ $ip -eq $it ]; then
                echo -e "  ${C}IMP${N}  ${G}QA ✅  $ip/$it passed${N}"
                sync_type "$control" "IMP" "$dry"
                ((synced++)) || true
            else
                echo -e "  ${C}IMP${N}  ${R}QA ⭕  $ip/$it — BLOCKED${N}"
            fi
        fi
    fi

    # ── SCR ──
    if [ -d "$ctrl_dir/SCR" ]; then
        read sp st <<< $(scr_qa_counts "$ctrl_dir")
        if [ $st -gt 0 ]; then
            if [ $sp -eq $st ]; then
                echo -e "  ${C}SCR${N}  ${G}QA ✅  $sp/$st passed${N}"
                sync_type "$control" "SCR" "$dry"
                ((synced++)) || true
            else
                echo -e "  ${C}SCR${N}  ${R}QA ⭕  $sp/$st — BLOCKED${N}"
            fi
        fi
    fi

    # ── REF ──
    if [ -d "$ctrl_dir/REF" ]; then
        read rp rt <<< $(ref_qa_counts "$ctrl_dir")
        if [ $rt -gt 0 ]; then
            if [ $rp -eq $rt ]; then
                echo -e "  ${C}REF${N}  ${G}QA ✅  $rp/$rt passed${N}"
                sync_type "$control" "REF" "$dry"
                ((synced++)) || true
            else
                echo -e "  ${C}REF${N}  ${R}QA ⭕  $rp/$rt — BLOCKED${N}"
            fi
        fi
    fi

    # ── CTX ──
    if [ -d "$ctrl_dir/CTX" ]; then
        read cp ct <<< $(ctx_qa_counts "$ctrl_dir")
        if [ $ct -gt 0 ]; then
            if [ $cp -eq $ct ]; then
                echo -e "  ${C}CTX${N}  ${G}QA ✅  $cp/$ct passed${N}"
                sync_type "$control" "CTX" "$dry"
                ((synced++)) || true
            else
                echo -e "  ${C}CTX${N}  ${R}QA ⭕  $cp/$ct — BLOCKED${N}"
            fi
        fi
    fi

    # ── FORM ──
    if [ -d "$ctrl_dir/FORM" ]; then
        read fp ft <<< $(form_qa_counts "$ctrl_dir")
        if [ $ft -gt 0 ]; then
            if [ $fp -eq $ft ]; then
                echo -e "  ${C}FORM${N} ${G}QA ✅  $fp/$ft passed${N}"
                sync_type "$control" "FORM" "$dry"
                ((synced++)) || true
            else
                echo -e "  ${C}FORM${N} ${R}QA ⭕  $fp/$ft — BLOCKED${N}"
            fi
        fi
    fi

    # ── INS ──
    if [ -d "$ctrl_dir/INS" ]; then
        read np nt <<< $(ins_qa_counts "$ctrl_dir")
        if [ $nt -gt 0 ]; then
            if [ $np -eq $nt ]; then
                echo -e "  ${C}INS${N}  ${G}QA ✅  $np/$nt passed${N}"
                sync_type "$control" "INS" "$dry"
                ((synced++)) || true
            else
                echo -e "  ${C}INS${N}  ${R}QA ⭕  $np/$nt — BLOCKED${N}"
            fi
        fi
    fi

    # ── WKBK (no QA gate — synced if directory exists with content) ──
    if [ -d "$ctrl_dir/WKBK" ]; then
        echo -e "  ${C}WKBK${N} ${G}→ sync (no QA gate)${N}"
        sync_type "$control" "WKBK" "$dry"
        ((synced++)) || true
    fi

    echo ""
    [ $synced -eq 0 ] && echo -e "  ${R}Nothing synced.${N}"
    [ $synced -gt 0 ] && [ "$dry" = "no" ] && echo -e "  ${G}✅ Done — synced to $category/$control/${N}"
    [ $synced -gt 0 ] && [ "$dry" = "yes" ] && echo -e "  ${Y}Dry run complete${N}"
    echo ""
}

# ─────────────────────────────────────────────────────────────────────────────
# PROMOTE ALL
# ─────────────────────────────────────────────────────────────────────────────
cmd_promote_all() {
    local dry="$1"
    local n_sync=0 n_skip=0
    local current_category=""

    echo ""
    echo -e "${B}════════════════════════════════════════════════════════════════════════════════${N}"
    echo -e "${B}  Batch Promote — All Controls (from 50-isms-core-framework)${N}"
    [ "$dry" = "yes" ] && echo -e "  ${Y}★ DRY RUN ★${N}"
    echo -e "${B}════════════════════════════════════════════════════════════════════════════════${N}"
    echo ""

    for ctrl in $(get_controls); do
        local category=$(get_category "$ctrl")
        local ctrl_dir
        ctrl_dir=$(find_control_dir "$ctrl") || continue

        if [ "$category" != "$current_category" ]; then
            [ -n "$current_category" ] && echo ""
            echo -e "  ${B}━━━ $category ━━━${N}"
            current_category="$category"
        fi

        read pp pt <<< $(pol_qa_counts "$ctrl_dir")
        read ip it <<< $(imp_qa_counts "$ctrl_dir")
        read sp st <<< $(scr_qa_counts "$ctrl_dir")
        read rp rt <<< $(ref_qa_counts "$ctrl_dir")
        read cp ct <<< $(ctx_qa_counts "$ctrl_dir")
        read fp ft <<< $(form_qa_counts "$ctrl_dir")
        read np nt <<< $(ins_qa_counts "$ctrl_dir")

        local pol=false imp=false scr=false ref=false ctx=false form=false ins=false
        [ $pt -gt 0 ] && [ $pp -eq $pt ] && pol=true
        [ $it -gt 0 ] && [ $ip -eq $it ] && imp=true
        [ $st -gt 0 ] && [ $sp -eq $st ] && scr=true
        [ $rt -gt 0 ] && [ $rp -eq $rt ] && ref=true
        [ $ct -gt 0 ] && [ $cp -eq $ct ] && ctx=true
        [ $ft -gt 0 ] && [ $fp -eq $ft ] && form=true
        [ $nt -gt 0 ] && [ $np -eq $nt ] && ins=true
        local wkbk=false
        [ -d "$ctrl_dir/WKBK" ] && wkbk=true

        local sn=$(short_name "$ctrl")

        if [ "$pol" = true ] || [ "$imp" = true ] || [ "$scr" = true ] || [ "$ref" = true ] || [ "$ctx" = true ] || [ "$form" = true ] || [ "$ins" = true ] || [ "$wkbk" = true ]; then
            echo -e "    ${G}→${N} $sn"
            [ "$pol" = true ]  && sync_type "$ctrl" "POL" "$dry"
            [ "$imp" = true ]  && sync_type "$ctrl" "IMP" "$dry"
            [ "$scr" = true ]  && sync_type "$ctrl" "SCR" "$dry"
            [ "$ref" = true ]  && sync_type "$ctrl" "REF" "$dry"
            [ "$ctx" = true ]  && sync_type "$ctrl" "CTX" "$dry"
            [ "$form" = true ] && sync_type "$ctrl" "FORM" "$dry"
            [ "$ins" = true ]  && sync_type "$ctrl" "INS" "$dry"
            [ "$wkbk" = true ] && sync_type "$ctrl" "WKBK" "$dry"
            ((n_sync++)) || true
        else
            echo -e "    ${D}⏭  $sn${N}"
            ((n_skip++)) || true
        fi
    done

    echo ""
    echo -e "  ${G}Synced: $n_sync${N}    ${D}Skipped: $n_skip${N}"
    [ "$dry" = "yes" ] && echo -e "  ${Y}(dry run — nothing written)${N}"
    echo ""
}

# ─────────────────────────────────────────────────────────────────────────────
# PROMOTE ALL OP-POLs (Operational product)
# Syncs 10-isms-core-operational/ → factory_isms/isms-core-operational/
# ─────────────────────────────────────────────────────────────────────────────
cmd_promote_operational() {
    local dry="$1"
    local n_sync=0

    echo ""
    echo -e "${B}════════════════════════════════════════════════════════════════════════════════${N}"
    echo -e "${B}  Promote Operational — Full Product (from 10-isms-core-operational)${N}"
    [ "$dry" = "yes" ] && echo -e "  ${Y}★ DRY RUN ★${N}"
    echo -e "${B}════════════════════════════════════════════════════════════════════════════════${N}"
    echo ""

    # ── Shared engine (A.0-checklist-engine/) ──
    local engine_src="$OP_SRC/A.0-checklist-engine"
    if [ -d "$engine_src" ]; then
        local engine_dst="$OP_DST/A.0-checklist-engine"
        local flags=(-a --delete "${EXCL[@]}")
        [ "$dry" = "yes" ] && flags+=(-n)
        mkdir -p "$engine_dst"
        echo -e "  ${C}A.0-checklist-engine${N}  ${G}→ sync shared engine${N}"
        rsync "${flags[@]}" "$engine_src/" "$engine_dst/" 2>&1 | sed 's/^/      /'
    fi

    echo ""

    # ── Per-control: POL + SCR + WKBK ──
    for section_dir in "$OP_SRC"/A.*; do
        [ -d "$section_dir" ] || continue
        local section=$(basename "$section_dir")
        echo -e "  ${B}━━━ $section ━━━${N}"

        for ctrl_dir in "$section_dir"/isms-*; do
            [ -d "$ctrl_dir" ] || continue
            local ctrl=$(basename "$ctrl_dir")
            local sn=$(short_name "$ctrl")
            local synced_types=""

            local flags=(-a --delete "${EXCL[@]}")
            [ "$dry" = "yes" ] && flags+=(-n)

            # POL
            local pol_dir="$ctrl_dir/POL"
            if [ -d "$pol_dir" ]; then
                local n_pol=0
                for f in "$pol_dir"/ISMS-OP-POL-*.md; do
                    [ -f "$f" ] || continue
                    ((n_pol++)) || true
                done
                if [ $n_pol -gt 0 ]; then
                    local dst="$OP_DST/$section/$ctrl/POL"
                    mkdir -p "$dst"
                    rsync "${flags[@]}" "$pol_dir/" "$dst/" 2>&1 | sed 's/^/      /'
                    synced_types+="POL "
                fi
            fi

            # SCR
            local scr_dir="$ctrl_dir/SCR"
            if [ -d "$scr_dir" ]; then
                local dst="$OP_DST/$section/$ctrl/SCR"
                mkdir -p "$dst"
                rsync "${flags[@]}" "$scr_dir/" "$dst/" 2>&1 | sed 's/^/      /'
                synced_types+="SCR "
            fi

            # WKBK
            local wkbk_dir="$ctrl_dir/WKBK"
            if [ -d "$wkbk_dir" ]; then
                local dst="$OP_DST/$section/$ctrl/WKBK"
                mkdir -p "$dst"
                rsync "${flags[@]}" "$wkbk_dir/" "$dst/" 2>&1 | sed 's/^/      /'
                synced_types+="WKBK "
            fi

            if [ -n "$synced_types" ]; then
                echo -e "    ${G}→${N} $sn (${synced_types% })"
                ((n_sync++)) || true
            fi
        done
    done

    echo ""
    echo -e "  ${G}Synced: $n_sync control groups${N}"
    [ "$dry" = "yes" ] && echo -e "  ${Y}(dry run — nothing written)${N}"
    echo ""
}

# ─────────────────────────────────────────────────────────────────────────────
# PROMOTE PRIVACY PRODUCT (ISO 27701:2025)
# Syncs 51-isms-core-privacy/ → factory_isms/isms-core-privacy/
# Full product rsync — promotes all subdirectories wholesale
# ─────────────────────────────────────────────────────────────────────────────
cmd_promote_privacy() {
    local dry="$1"

    echo ""
    echo -e "${B}════════════════════════════════════════════════════════════════════════════════${N}"
    echo -e "${B}  Promote Privacy — Full Product (ISO 27701:2025)${N}"
    echo -e "${B}  Source: 51-isms-core-privacy/${N}"
    echo -e "${B}  Target: factory_isms/isms-core-privacy/${N}"
    [ "$dry" = "yes" ] && echo -e "  ${Y}★ DRY RUN ★${N}"
    echo -e "${B}════════════════════════════════════════════════════════════════════════════════${N}"
    echo ""

    if [ ! -d "$PRIV_SRC" ]; then
        echo -e "  ${R}Source not found: $PRIV_SRC${N}" >&2
        exit 1
    fi

    local flags=(-a --delete "${EXCL[@]}")
    [ "$dry" = "yes" ] && flags+=(-n)
    mkdir -p "$PRIV_DST"

    local n_sync=0
    for subdir in "$PRIV_SRC"/*/; do
        [ -d "$subdir" ] || continue
        local name=$(basename "$subdir")
        echo -e "  ${C}$name${N}  ${G}→ sync${N}"
        rsync "${flags[@]}" "$subdir" "$PRIV_DST/$name/" 2>&1 | sed 's/^/      /'
        ((n_sync++)) || true
    done

    echo ""
    echo -e "  ${G}Synced: $n_sync subdirectories${N}"
    [ "$dry" = "yes" ] && echo -e "  ${Y}(dry run — nothing written)${N}"
    echo ""
}

# ─────────────────────────────────────────────────────────────────────────────
# PROMOTE CLOUD PRODUCT (ISO 27018:2025)
# Syncs 52-isms-core-cloud/ → factory_isms/isms-core-cloud/
# Full product rsync — promotes all subdirectories wholesale
# ─────────────────────────────────────────────────────────────────────────────
cmd_promote_cloud() {
    local dry="$1"

    echo ""
    echo -e "${B}════════════════════════════════════════════════════════════════════════════════${N}"
    echo -e "${B}  Promote Cloud — Full Product (ISO 27018:2025)${N}"
    echo -e "${B}  Source: 52-isms-core-cloud/${N}"
    echo -e "${B}  Target: factory_isms/isms-core-cloud/${N}"
    [ "$dry" = "yes" ] && echo -e "  ${Y}★ DRY RUN ★${N}"
    echo -e "${B}════════════════════════════════════════════════════════════════════════════════${N}"
    echo ""

    if [ ! -d "$CLD_SRC" ]; then
        echo -e "  ${R}Source not found: $CLD_SRC${N}" >&2
        exit 1
    fi

    local flags=(-a --delete "${EXCL[@]}")
    [ "$dry" = "yes" ] && flags+=(-n)
    mkdir -p "$CLD_DST"

    local n_sync=0
    for subdir in "$CLD_SRC"/*/; do
        [ -d "$subdir" ] || continue
        local name=$(basename "$subdir")
        echo -e "  ${C}$name${N}  ${G}→ sync${N}"
        rsync "${flags[@]}" "$subdir" "$CLD_DST/$name/" 2>&1 | sed 's/^/      /'
        ((n_sync++)) || true
    done

    echo ""
    echo -e "  ${G}Synced: $n_sync subdirectories${N}"
    [ "$dry" = "yes" ] && echo -e "  ${Y}(dry run — nothing written)${N}"
    echo ""
}

# ─────────────────────────────────────────────────────────────────────────────
# PROMOTE SEC PRODUCT (ISO 27017:2025 — FUTURE)
# Syncs 53-isms-core-sec/ → factory_isms/isms-core-sec/
# Placeholder — product not yet built
# ─────────────────────────────────────────────────────────────────────────────
cmd_promote_sec() {
    local dry="$1"

    echo ""
    echo -e "${B}════════════════════════════════════════════════════════════════════════════════${N}"
    echo -e "${B}  Promote SEC — Full Product (ISO 27017:2025)${N}"
    echo -e "${B}  Source: 53-isms-core-sec/${N}"
    echo -e "${B}  Target: factory_isms/isms-core-sec/${N}"
    [ "$dry" = "yes" ] && echo -e "  ${Y}★ DRY RUN ★${N}"
    echo -e "${B}════════════════════════════════════════════════════════════════════════════════${N}"
    echo ""

    if [ ! -d "$SEC_SRC" ]; then
        echo -e "  ${Y}⚠  Source not found: $SEC_SRC${N}"
        echo -e "  ${D}SEC product (ISO 27017:2025) not yet built. Nothing to promote.${N}"
        echo ""
        return 0
    fi

    local flags=(-a --delete "${EXCL[@]}")
    [ "$dry" = "yes" ] && flags+=(-n)
    mkdir -p "$SEC_DST"

    local n_sync=0
    for subdir in "$SEC_SRC"/*/; do
        [ -d "$subdir" ] || continue
        local name=$(basename "$subdir")
        echo -e "  ${C}$name${N}  ${G}→ sync${N}"
        rsync "${flags[@]}" "$subdir" "$SEC_DST/$name/" 2>&1 | sed 's/^/      /'
        ((n_sync++)) || true
    done

    echo ""
    echo -e "  ${G}Synced: $n_sync subdirectories${N}"
    [ "$dry" = "yes" ] && echo -e "  ${Y}(dry run — nothing written)${N}"
    echo ""
}

# ─────────────────────────────────────────────────────────────────────────────
# PROMOTE AI PRODUCT (ISO/IEC 42001:2023)
# Syncs 53-isms-core-ai/ → factory_isms/isms-core-ai/
# Full product rsync — promotes all subdirectories wholesale
# ─────────────────────────────────────────────────────────────────────────────
cmd_promote_ai() {
    local dry="$1"

    echo ""
    echo -e "${B}════════════════════════════════════════════════════════════════════════════════${N}"
    echo -e "${B}  Promote AI — Full Product (ISO/IEC 42001:2023)${N}"
    echo -e "${B}  Source: 53-isms-core-ai/${N}"
    echo -e "${B}  Target: factory_isms/isms-core-ai/${N}"
    [ "$dry" = "yes" ] && echo -e "  ${Y}★ DRY RUN ★${N}"
    echo -e "${B}════════════════════════════════════════════════════════════════════════════════${N}"
    echo ""

    if [ ! -d "$AI_SRC" ]; then
        echo -e "  ${R}Source not found: $AI_SRC${N}" >&2
        exit 1
    fi

    local flags=(-a --delete "${EXCL[@]}")
    [ "$dry" = "yes" ] && flags+=(-n)
    mkdir -p "$AI_DEST"

    local n_sync=0
    for subdir in "$AI_SRC"/*/; do
        [ -d "$subdir" ] || continue
        local name=$(basename "$subdir")
        echo -e "  ${C}$name${N}  ${G}→ sync${N}"
        rsync "${flags[@]}" "$subdir" "$AI_DEST/$name/" 2>&1 | sed 's/^/      /'
        ((n_sync++)) || true
    done

    echo ""
    echo -e "  ${G}Synced: $n_sync subdirectories${N}"
    [ "$dry" = "yes" ] && echo -e "  ${Y}(dry run — nothing written)${N}"
    echo ""
}

# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────
main() {
    if [ $# -eq 0 ]; then
        echo ""
        echo "  Usage:"
        echo "    ./promote_control.sh <control>              # Promote single Framework control"
        echo "    ./promote_control.sh --all                  # Promote all Framework controls"
        echo "    ./promote_control.sh --operational           # Promote Operational product"
        echo "    ./promote_control.sh --privacy               # Promote Privacy product (ISO 27701:2025)"
        echo "    ./promote_control.sh --cloud                 # Promote Cloud product (ISO 27018:2025)"
        echo "    ./promote_control.sh --sec                   # Promote SEC product (ISO 27017:2025)"
        echo "    ./promote_control.sh --ai                    # Promote AI product (ISO/IEC 42001:2023)"
        echo "    ./promote_control.sh --status               # QA status dashboard"
        echo "    ./promote_control.sh --dry-run <any>        # Preview without writing"
        echo ""
        echo "  Sources:"
        echo "    50-isms-core-framework/  → factory_isms/isms-core-framework/"
        echo "    10-isms-core-operational/ → factory_isms/isms-core-operational/"
        echo "    51-isms-core-privacy/    → factory_isms/isms-core-privacy/"
        echo "    52-isms-core-cloud/      → factory_isms/isms-core-cloud/"
        echo "    52-isms-core-cloud/      → factory_isms/isms-core-sec/  (future)"
        echo "    53-isms-core-ai/         → factory_isms/isms-core-ai/"
        echo ""
        exit 0
    fi

    local dry="no"
    local args=()
    for a in "$@"; do
        [ "$a" = "--dry-run" ] && { dry="yes"; continue; }
        args+=("$a")
    done

    case "${args[0]:-}" in
        --status)       cmd_status ;;
        --all)          cmd_promote_all "$dry" ;;
        --operational)  cmd_promote_operational "$dry" ;;
        --privacy)      cmd_promote_privacy "$dry" ;;
        --cloud)        cmd_promote_cloud "$dry" ;;
        --sec)          cmd_promote_sec "$dry" ;;
        --ai)           cmd_promote_ai "$dry" ;;
        isms-*)         cmd_promote "${args[0]}" "$dry" ;;
        *)              echo -e "${R}Unknown: ${args[0]}${N}" >&2; exit 1 ;;
    esac
}

main "$@"
