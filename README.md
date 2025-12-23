# LumiLearn AI - Learning Management Platform

A modern, AI-driven learning management platform with a ChatGPT-inspired interface, designed to help students manage their classes, track progress, and interact with an AI learning assistant.

## Project Overview

LumiLearn AI is a full-stack application built with Next.js (frontend) and Python (backend), featuring a purple-themed, minimalist design inspired by NotebookLM and ChatGPT.

## Features Implemented

### 1. Dashboard (Main Page - `/`)
- **Google Classroom-style Interface**: Clean grid layout showing all classes
- **Create Class Button**: Prominent button to add new classes
- **Empty State**: Proactive messaging when no classes exist
- **Class Cards**: Display course information with:
  - Mastery progress bars
  - Next milestone information
  - Quick access to PDFs and memory graphs
- **Purple Theme**: Consistent #e6e6ff background throughout

### 2. Individual Class Pages (`/classes/[id]`)
- **Focused Course Management**: Minimalist cockpit for single course management
- **Compact Header**: Class title and next deadline status
- **Grading Sidebar**: 
  - Fixed vertical sidebar on the right
  - Displays grading weights from syllabus (e.g., Participation: 10%, Midterm: 30%)
  - Collapsible/expandable with toggle button
  - Smooth animations
- **Materials List**: PDFs and notes organized by course
- **Deadlines List**: Upcoming tasks, exams, and assignments with:
  - Date formatting
  - Days remaining calculation
  - Color-coded by type (exam, assignment, other)
- **Send to Calendar Button**: 
  - Conditional verification for exam/deadline dates
  - 2-second loading animation
  - Success message with checkmark
- **Back Button**: Navigate back to dashboard

### 3. Sidebar Navigation
- **Persistent State**: Sidebar remains open/closed across page navigation
- **Top Icons**:
  - Close sidebar (left)
  - Create new class "+" button (middle-right)
  - LumiLearnAI chat navigation (right)
- **Navigation Links**:
  - Dashboard (main page)
  - LumiLearnAI (chat interface)
  - Calendar
- **Sign In/Sign Up Button**: 
  - Black button with white text
  - White background on hover
  - Opens authentication modal

### 4. Authentication Modal
- **ChatGPT-Style Design**: 
  - Centered white modal on purple background
  - Toggle bar at top with Sign In/Sign Up options
  - Sliding indicator for active option
  - Smooth transitions
- **Back Button**: Visible back button with label at top of modal
- **Form Fields**:
  - Sign In: Email, Password
  - Sign Up: Name, Email, Password, Confirm Password
- **Purple Theme**: All buttons and interactive elements use purple shades
- **No Click-to-Close**: Background doesn't close modal (only back button)

### 5. LumiLearnAI Chat Page (`/chat`)
- **Chat Interface**: Full ChatGPT-like interface
- **Input Area**: Large, minimalist input with microphone icon
- **Action Pills**: Quick actions like "Quick Recall Drill" and "Plan My Day"
- **Purple Theme**: Consistent with rest of application

### 6. Calendar Page (`/calendar`)
- **Calendar View**: Placeholder for calendar functionality
- **Consistent Layout**: Same sidebar and top section as other pages

## Technical Architecture

### Frontend Stack
- **Framework**: Next.js 14+ (App Router)
- **UI Library**: Chakra UI v3
- **Language**: TypeScript
- **State Management**: React Context API
- **Styling**: Chakra UI with custom purple theme

### Key Components

#### Context Providers
- `SidebarProvider`: Manages sidebar visibility state
- `ClassProvider`: Manages course/class data
- `ModalProvider`: Manages modal states (create class, auth)

#### Main Components
- `Sidebar`: Navigation sidebar with collapsible functionality
- `TopSection`: Header bar with hamburger menu
- `CourseGrid`: Grid layout for displaying classes
- `CourseCard`: Individual class card component
- `GradingSidebar`: Fixed sidebar showing grading breakdown
- `MaterialsList`: List of course materials
- `DeadlinesList`: List of upcoming deadlines
- `AuthModal`: Sign in/sign up modal
- `CreateClassModal`: Modal for creating new classes

### Color Palette
- **Background**: #e6e6ff (light purple/lavender)
- **Sidebar**: #c7c7ff (medium purple)
- **Accent Purple**: #8b5cf6 (primary actions)
- **Darker Purple**: #7c3aed (hover states)
- **Lighter Purple**: #a78bfa (subtle accents)
- **Text**: #111827 (dark), #6b7280 (muted)
- **Buttons**: Black (#111827) with white text for sidebar

### File Structure
```
frontend/app/
├── page.tsx                    # Main dashboard (class list)
├── chat/
│   └── page.tsx               # LumiLearnAI chat interface
├── classes/
│   ├── page.tsx               # Redirects to dashboard
│   └── [id]/
│       └── page.tsx           # Individual class page
├── calendar/
│   └── page.tsx               # Calendar view
├── signin/
│   └── page.tsx               # Sign in page (placeholder)
├── signup/
│   └── page.tsx               # Sign up page (placeholder)
├── components/
│   ├── auth/
│   │   └── auth-modal.tsx    # Authentication modal
│   ├── chatgpt-ui/
│   │   ├── sidebar.tsx        # Main sidebar
│   │   ├── sidebar-context.tsx
│   │   ├── top-section.tsx
│   │   ├── middle-section.tsx
│   │   └── bottom-section.tsx
│   ├── classes/
│   │   ├── class-context.tsx  # Course data management
│   │   ├── modal-context.tsx  # Modal state management
│   │   ├── course-card.tsx
│   │   ├── course-grid.tsx
│   │   ├── create-class-modal.tsx
│   │   ├── grading-sidebar.tsx
│   │   ├── materials-list.tsx
│   │   ├── deadlines-list.tsx
│   │   └── send-to-calendar-button.tsx
│   └── dashboard/
│       ├── todays-mission.tsx
│       ├── learning-action-bar.tsx
│       └── daily-tasks.tsx
└── icons/
    ├── sidebar-icons.tsx
    ├── dashboard-icons.tsx
    └── other-icons.tsx
```

## Data Models

### Course Interface
```typescript
interface Course {
  id: string;
  name: string;
  masteryProgress: number; // 0-100
  nextMilestone: {
    name: string;
    daysRemaining: number;
  };
  pdfUrl?: string;
  memoryGraphUrl?: string;
  gradingWeights?: GradingWeight[];
  materials?: Material[];
  deadlines?: Deadline[];
}
```

## Recent Updates

### Latest Changes
1. **Sidebar Updates**:
   - Replaced separate Sign In/Sign Up buttons with single button
   - Button opens modal instead of navigating to pages
   - Changed button color to black with white hover effect
   - Grouped "+" button with LumiLearnAI button on right side

2. **Auth Modal Enhancements**:
   - Added visible back button with label
   - Changed all blue colors to purple theme
   - Removed click-to-close on background
   - ChatGPT-style toggle with sliding indicator

3. **Class Page Improvements**:
   - Added collapsible grading sidebar
   - Improved layout responsiveness
   - Enhanced deadline and materials display

4. **Dashboard Refactoring**:
   - Transformed from learning dashboard to class list
   - Google Classroom-style interface
   - Moved learning features to individual class pages

## Development Notes

### State Management
- Sidebar state persists across page navigation via `SidebarProvider` in root layout
- Class data managed through `ClassProvider` context
- Modal states (create class, auth) managed through `ModalProvider`

### Design Principles
- Monochromatic palette with purple accent color
- NotebookLM-inspired aesthetic
- Minimalist, clean interface
- Consistent spacing and typography
- Smooth transitions and animations

## Future Enhancements

- Backend integration for authentication
- Real course data from API
- Calendar integration
- AI chat functionality
- File upload and processing
- Progress tracking and analytics

## Getting Started

### Prerequisites
- Node.js 18+
- npm or yarn

### Installation
```bash
cd frontend
npm install
npm run dev
```

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Project Status

✅ **Completed**:
- Dashboard with class grid
- Individual class pages
- Sidebar navigation
- Authentication modal UI
- Grading sidebar with toggle
- Materials and deadlines lists
- Create class modal
- Responsive design
- Purple theme implementation

🚧 **In Progress**:
- Backend API integration
- Authentication logic
- Calendar functionality

📋 **Planned**:
- AI chat features
- File processing
- Progress analytics
- User profiles
