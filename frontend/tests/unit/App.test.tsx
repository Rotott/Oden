import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import App from '../../src/App';

describe('App', () => {
  // Test setup placeholder. PASS
  it('renders the ODEN heading', () => {
    render(<App />);

    expect(screen.getByRole('heading', { name: 'Hello from ODEN' })).toBeInTheDocument();
  });


});
